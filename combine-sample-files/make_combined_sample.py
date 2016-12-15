#!/usr/bin/python
import csv

# USAGE
# create a file sample_paths.txt containing the full paths to each sample
# then run ./make_combined_sample.py
# it will create combined_samples.tsv file 
# then upload it as normal


# sample list has paths to samples, 1 per line

SAMPLE_LIST = "sample_paths.txt"
RESULT_FILE = "combined_samples.tsv"

# Takes sample filename
# and tab-separated column
# returns that column as an array
def getSampleColumn(sample, column):
   res = []
   with open(sample, "r") as s:
      r = csv.reader(s, delimiter="\t")
      for line in r:
         res.append(line[column])
   return res 

def getSampleGenes(sample):
   return getSampleColumn(sample, 0)

def getSampleValues(sample):
   return getSampleColumn(sample, 1)

# confirm the sample's genes matches
# the passed gene list
def confirmGenes(sample, genes):
   sample_genes = getSampleGenes(sample)
   if(sample_genes == genes):
      # return the sample values
      return getSampleValues(sample)
   else:
      return False

def main():
   print "Input: sample_paths.txt"
   print "output: combined_samples.tsv"
   print "Samples MUST all be destined for the same data set & study,"
   print "and must all have the same normalization."
  
   # result array
   # 1st line = gene list
   # each additional line is a sample
   # when we write it, we turn it "sideways" 
   genes = []
   result = []
   with open(SAMPLE_LIST, "r") as samples:
      for s in samples:
         sample = s.rstrip()
         if len(genes) == 0:
            genes = getSampleGenes(sample)
         # get the values
         sample_values = confirmGenes(sample, genes)
         # will either be an array of the column to add, or False
         if(sample_values):
            result.append(sample_values)
            # add the values to the result array
         else:
            print "SKIPPED SAMPLE: genes did not match: %s" % sample

      # Then, write out the result
      with open(RESULT_FILE, "w") as result_file:
         writer=csv.writer(result_file, delimiter="\t", lineterminator="\n")
         for i in range(0, len(genes)):
            # get the current gene
            this_gene = [genes[i]]
            # also make an array that is just the items 
            # at index i
            current_line = map(lambda x: x[i], result)
            writer.writerow(this_gene + current_line)

   print("done!")
if __name__ == '__main__' :
   main()
