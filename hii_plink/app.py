from os.path import abspath, basename, dirname, exists, join, splitext

import subprocess
from subprocess import PIPE

def remove_duplicates(args):

    plink_fname = args['plink_prefix']
    output_prefix = args['output_prefix']

    file_name=splitext(basename(plink_fname))[0]

    # convert to vcf
    command = f'plink --bfile {plink_fname} --recode vcf --out {output_prefix}/{file_name}'
    subprocess.call(command, shell=True)
    print("Finished converting to VCF")

    # remove dups using bcftools
    command = f'bcftools norm --rm-dup all -o {output_prefix}/{file_name}_no_dups.vcf -O vcf {output_prefix}/{file_name}.vcf'
    subprocess.call(command, shell=True)
    print("Finished removing duplicate snps using Bcftools")

    # convert to vcf to plink
    command = f'plink --vcf {output_prefix}/{file_name}_no_dups.vcf --const-fid --make-bed --out {output_prefix}/{file_name}_no_dups'
    subprocess.call(command, shell=True)
    print("Finished converting VCF back to Plink")

    # set fam IDs back to original
    command = f'cut -d" " -f1-2 {output_prefix}/{file_name}_no_dups.fam > {output_prefix}/new_fam_ids.txt'
    command2 = f'cut -d" " -f1-2 {plink_fname}.fam > {output_prefix}/ori_fam_ids.txt'
    command3 = f'paste -d" " {output_prefix}/new_fam_ids.txt {output_prefix}/ori_fam_ids.txt > {output_prefix}/update_fam_ids.txt'

    subprocess.call(command, shell=True)
    subprocess.call(command2, shell=True)
    subprocess.call(command3, shell=True)

    command = f'plink --bfile {output_prefix}/{file_name}_no_dups --update-ids {output_prefix}/update_fam_ids.txt --make-bed --out {output_prefix}/{file_name}_no_dups_final'
    subprocess.call(command, shell=True)
    print("Finished fixing Fam IDs")
    print("***** COMPLETE ******")


def snpid_from_coord_update(args):
    pass

def snpid_and_position_update(args):
    pass
