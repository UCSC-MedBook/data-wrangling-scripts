#!/bin/bash

# IF the directories aren't group writable --
# let's fix that
# this makes writable the Hugo directories only
# (you must have permissions to change this of course)
# pass this the base dir
# and then the list of sample IDs

while read line; do
   chmod g+w $1/$line/rnaseq/RSEM/Hugo
done < $2
