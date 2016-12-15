[migrated from [sui-generum](https://github.com/e-t-k/sui-generum/commit/802e20d6fa07b66529d385f7c57e1f12fd7346da?diff=unified)]

How to prepare the sample files for make_combined_sample.py

1. Untar containers, find files, list paths

for file in *.tar.gz ; do tar -zvxf $file; done
find . -name "rsem.genes.norm_counts.hugo.tab" > sample_paths.txt

2. Get the script

git clone https://github.com/e-t-k/sui-generum.git
mv sui-generum/make_combined_sample.py .

3. Run the script

./make_combined_sample.py

4. Upload the combined sample directly.
Replace SERVERNAME_HERE with the appropriate server.

curl -k https://SERVERNAME_HERE/cfs/files/blobs?filename=combined_samples.tsv -H "Content-Type: text/plain" -T combined_samples.tsv

5. You will receive an ID receipt; use this ID in the "blob import" field in wrangler.
EG: you get {"_id":"1234567890"} ; enter 1234567890 into the field.

6. To get the sample IDs directly from the file contents:
while read line; do head -n 1 $line | cut -f2; done < sample_paths.txt > sample_ids.txt
