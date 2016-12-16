#!/bin/bash

# This script places the TPM/hugo result files in the folder
# with the original RNASeq output.
# it makes a lot of assumptions about the location of everything.
# Inputs are :
# $1 is the basedir to put them back in
# $2 is the file containing each sample ID. 
# The outputs are assumed to be in hugo.output within the pwd
# and named SAMPLENAME.tpm.tab.output.tsv

# it will put them in $samplename/rnaseq/RSEM/Hugo
# named rsem.genes.tpm.hugo.tab

while read line; do
   cp hugo.output/$line.tpm.tab.output.tsv $1/$line/rnaseq/RSEM/Hugo/rsem.genes.tpm.hugo.tab
done < $2

echo "If you got permission denied errors, the target directory needs to be made group-writable."
