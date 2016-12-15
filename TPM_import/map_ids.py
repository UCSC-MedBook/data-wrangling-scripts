#!/usr/bin/python2.7

# requires 2.7 for DictWriter.writeheader()

import csv
from decimal import * # only for this stupid zeroes dropping thing

# Given a tsv file,
# maps items in the first column to new values as provided by a dictionary.
# Items with missing keys are dropped

# Example : map a sample with ensembl IDs to Hugo gene names

# INPUTS : todo dont hardcode

MAPPING_FILE="EnsGeneID_Hugo_Observed_Conversions.txt"
# New values in FIRST column
# Old values in SECOND column
# tab separated


INPUT_FILE="sample.tsv"
OUTPUT_FILE="output.tsv"

MAPPED_COLUMN_HEADER="gene_id"
# If your old value maps to this key, drop the line anyhow
# we'll also drop any lines where key is not found in the mapping file
NEW_VALUE_TO_SKIP="NA"


# This should be false unless you completely understand what it is for.
# When we're testing this, we run it on a norm_counts output and compare it to the 
# already-hugoe'd version of that output. But whatever hugo translation the rna-seq
# is running does some weird normalization and dropping of zeroes at the end of numbers
# so we need to duplicate that when we're testing so that we don't get spurious diffs.
UNNECESSARILY_DROP_ZEROES=True


def main():

  dropped_lines_count = 0

  # load the mapping
  with open(MAPPING_FILE, "r") as mapping:
    reader = csv.reader(mapping, delimiter="\t")
    old_values_to_new=dict((r[1],r[0]) for r in reader) # note that new values are r[0] not r[1]

  # Process the file
  with open(INPUT_FILE, "r") as i:
    input_lines = csv.DictReader(i, delimiter='\t')

    with open(OUTPUT_FILE, 'w') as o:
      output_lines = csv.DictWriter(o, input_lines.fieldnames, delimiter='\t', lineterminator='\n')
      output_lines.writeheader()

      for line in input_lines:

        if UNNECESSARILY_DROP_ZEROES:
          dataval = line[input_lines.fieldnames[1]]
          # Normalize it to drop extra zeroes, then format it as 'f' to remove scientific notation
          zeroes_dropped = format(Decimal(dataval).normalize(), "f")
          # but add one on if we lost the decimal
          if '.' not in zeroes_dropped:
            zeroes_dropped = zeroes_dropped + '.0'
          
          line[input_lines.fieldnames[1]] = zeroes_dropped
          

        old_value = line[MAPPED_COLUMN_HEADER]
        if (old_value in old_values_to_new) and (old_values_to_new[old_value] != NEW_VALUE_TO_SKIP):
          line[MAPPED_COLUMN_HEADER] = old_values_to_new[old_value] 
          output_lines.writerow(line)
        else:
          # drop the line and update count
          dropped_lines_count += 1
          try:
            print "dropped {} which mapped to {}".format(old_value, old_values_to_new[old_value])
          except KeyError, e:
            print "dropped {} not found in mapping file".format(old_value)
          # comment?


  print "dropped {} lines due to no key".format(dropped_lines_count)


if __name__ == '__main__':
  main()
