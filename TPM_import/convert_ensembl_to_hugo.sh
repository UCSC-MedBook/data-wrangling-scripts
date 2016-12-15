#!/bin/bash

# Usage :
# convert_ensembl_to_hugo.sh  "SAMPLEFILE"
# example:
# convert_ensembl_to_hugo.sh  "samples.txt"
# SAMPLEFILE should have one sample ID per line.
# Samples are searched for in folder output/ , filename sample_id.tpm.tab 

# (optimized for usage after extract_tpm_columm_from_rsem_genes.results.sh )

mkdir -p hugo.output

while read line; do 
   ./map_gene_id_column_features.py output/$line.tpm.tab
done < $1

mv output/*output.tsv hugo.output

# Also make a bonus sample_paths file for ease in combining samples.

find hugo.output -name "*tpm.tab.output.tsv" > sample_paths.txt
