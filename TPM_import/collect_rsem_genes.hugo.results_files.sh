#!/bin/bash

# Usage:
# have a file with two columns, tab separated
# column 1 : your sample ID, will be used as the filename
# column 2: the full path to the corresponding sample directory
# (The rsem_genes.hugo.results file is assumed to be in */RSEM/Hugo/rsem_genes.hugo.results)

if [ $# -lt 1 ]
  then
    echo "usage: ./collect_rsem_genes.hugo.results_files.sh sample_list_file"
    exit 1
fi


mkdir -p output

while read sampleid path; do 
   cp -vn $path/RSEM/Hugo/rsem_genes.hugo.results output/$sampleid \
      >> output/collect_files.out.log 2>>output/collect_files.err.log
done < $1
