# hii_plink

Streamlines various plink commands processes

## Requiremnets 
- python 3
- bcftools
- plink 

## Usage

      hii_plink <sub_command> [options...]

### remove_duplicates

Tool to remove duplicate snps inside of plink binary files bim, bed, and fam. Unlike using plink --list-duplicate-vars and --exlude to get rid of all snps that are duplicated, this tool keeps one copy of duplicated snps and removes the rest. This allows retenation of data without unncessary throwing it away.  

If you have plink files: test.bim, test.fam, test.bed 

plink_prefix = {input_dir}/test 

      hii_plink remove_duplicates --plink_prefix {plink_prefix} -o {output_dir}

##### Output 

      {output_dir}/test_no_dups_final.{bim,fam,bed}

### snpid_from_coord_update 

Uses snptk snpid_from_coord output to update plink files 

      hii_plink snpid_from_coord_update 
            --plink_prefix {plink_prefix} 
            --update_file {path_to_update_file} 
            --delete_file {path_to_delete_file} 
            -o {output_dir}
 
 ##### Output 

      {output_dir}/test_updated_final.{bim,fam,bed}

### snpid_and_position_update 

Uses snptk snpid_and_position output to update plink files 

      hii_plink snpid_and_position_update 
            --plink_prefix {plink_prefix} 
            --update_file {path_to_update_file} 
            --delete_file {path_to_delete_file} 
            --coord_file {path_to_file} 
            --chr_file {path_to_file} 
            -o {output_dir}
##### Output 

      {output_dir}/test_updated_final.{bim,fam,bed}
