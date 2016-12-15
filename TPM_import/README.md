### Importing TPM Data to MedBook

TPM data comes out of the RNA-Seq pipeline as a column in the `RSEM/rsem_genes.results` file.
It needs to undergo the following transformations - that do not apply to norm_counts data -- before being imported into MedBook:
* Extract TPM column and feature labels column from file
* Update header to contain sample ID
* Update feature labels from ensembl IDs to Hugo gene names

The following transformation wil lbe performed upon input into MedBook:
* expression data will be log<sub>2</sub>(n+1) normalized
* rows with duplicate feature labels will be merged (averaged together)


#### How to transform TPM data using these scripts
   1. Collect your sample IDs and add them to a file, one per line, eg *samples.txt*.
   2. Determine the path to your sample folders. eg */home/ubuntu/run10*
   3. Run `extract_tpm_columm_from_rsem_genes.results.sh` to create tpm sample files with two columns.
      This will create a folder `output` with a *samplename*.tpm.tab file for each sample.
    * `extract_tpm_columm_from_rsem_genes.results.sh "/home/ubuntu/run10" samples.txt

(TO BE CONTINUED)
