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
(TODO)
