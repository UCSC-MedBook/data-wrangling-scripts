#!/bin/bash

# Usage:
# have a file with two columns, tab separated
# column 1 : your sample ID, will be used in header and as filenaem
# column 2: the full paths to the corresponding rsem_genes.results file.

# eg sample_paths.txt
# Then run:

# extract_tpm_column_using_full_path.sh sample_paths.txt

# it will run and pull out the TPM info and add to the sample TPM file in "output" dir


mkdir -p output

while read sampleid path; do 
   # Output to confirm we're getting the correct columns 
   printf "Processing $sampleid, columns:"
   cut -f1,6 $path | head -n 1

   # Set the header to include the sample name
   printf "gene_id\t$sampleid\n" > output/$sampleid.tpm.tab;

   # Get the TPM column , chop off the old header(that says TPM) and add contents to file
   cut -f1,6 $path | tail -n +2 >> output/$sampleid.tpm.tab 
done < $1
