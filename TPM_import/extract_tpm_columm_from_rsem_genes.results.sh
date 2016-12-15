#!/bin/bash

# Usage :
# extract_tpm_columm_from_rsem_genes.results.sh "BASEDIR" "SAMPLEFILE"
# examples:
# extract_tpm_columm_from_rsem_genes.results.sh "/home/ubuntu/run10" "sample_names.txt" "rnaseq/RSEM/rsem_genes.results"
# SAMPLEFILE should have one sample ID per line.
# samples are searched for in "$BASEDIR/$SAMPLENAME/rnaseq/RSEM/rsem_genes.results"

mkdir -p output

while read line; do 
   # Output to confirm we're getting the correct columns 
   printf "Processing $line, columns:"
   cut -f1,6 $1/$line/rnaseq/RSEM/rsem_genes.results | head -n 1

   # Set the header to include the sample name
   printf "gene_id\t$line\n" > output/$line.tpm.tab;

   # Get the TPM column , chop off the old header(that says TPM) and add contents to file
   cut -f1,6 $1/$line/rnaseq/RSEM/rsem_genes.results | tail -n +2 >> output/$line.tpm.tab 
done < $2
