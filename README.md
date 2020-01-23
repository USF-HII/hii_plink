# plink_remove_dups
Tool to remove duplicate snps inside of plink binary files bim, bed, and fam. Unlike using plink --list-duplicate-vars and --exlude to get rid of all snps that are duplicated, this tool keeps one copy of duplicated snps and removes the rest. This allows retenation of data without unncessary throwing it away.  

### Requiremnets 
- python 3
- bcftools
- plink 

### Usage

If you have plink files: test.bim, test.fam, test.bed 

plink_prefix = {input_dir}/test 

`plink_remove_dups --plink_prefix {plink_prefix} -o {output_dir}` 

### Output 

`{output_dir}/test_no_dups_final.{bim,fam,bed}`
