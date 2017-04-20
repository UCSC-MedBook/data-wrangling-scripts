#!/bin/bash

# Collects ensembl results files, not hugo

# Usage:
# have a file with two columns, tab separated
# column 1 : your sample ID, will be used as the filename
# column 2: the full path to the corresponding sample directory
# (The rsem_genes.results file is assumed to be in */RSEM/rsem_genes.results)

if [ $# -lt 1 ]
  then
    echo "usage: ./collect_rsem_genes.ensembl.results_files.sh sample_list_file"
    exit 1
fi


mkdir -p output.ensembl

while read sampleid path; do 
   cp -vn $path/RSEM/rsem_genes.results output.ensembl/$sampleid \
      >> output.ensembl/collect_files.out.log 2>>output.ensembl/collect_files.err.log
done < $1
