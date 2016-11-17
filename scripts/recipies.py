#Extract reads by coverage

~/khmer/khmer/scripts/load-into-counting.py -x 1e8 -k 20 ecoli_reads.ct \
../seqs/ecoli_ref-5m.fastq.gz


~/khmer/khmer/scripts/abundance-dist.py ecoli_reads.ct ../seqs/ecoli_ref-5m.fastq.gz \
ecoli_reads.hist

#Estimate metagenome size from unassembled reads

~/khmer/khmer/scripts/normalize-by-median.py -k 20 -C 10 -x 1e8 -R metagenome_size_report.txt \
../seqs/ecoli_ref-5m.fastq.gz

~/khmer/khmer/scripts/estimate-genome-size.py -C 20 -k 20 ecoli_ref-5m.fastq.gz.keep metagenome_size_report.txt

#Estimate saturation of sequencing

~/khmer/khmer/sandbox/saturate-by-median.py -x 1e8 -k 20 -C 5 -R saturation_report.txt --report-frequency 10 \
../seqs/ecoli_ref-5m.fastq.gz

#Error-trim reads
~/khmer/khmer/scripts/load-into-counting.py -x 1e8 -k 20 ecoli_reads.kh \
../seqs/ecoli_ref-5m.fastq.gz
       
~/khmer/khmer/scripts/abundance-dist.py -s ecoli_reads.kh ../seqs/ecoli_ref-5m.fastq.gz ecoli_reads.dist

~/khmer/khmer/scripts/trim-low-abund.py -x 1e8 -k 20 ../seqs/ecoli_ref-5m.fastq.gz

#Trim metagenome and transcriptome reads with variable coverage k-mer trimming
~/khmer/khmer/scripts/trim-low-abund.py -x 1e8 -k 20 -V ../seqs/ecoli_ref-5m.fastq.gz
~/khmer/khmer/scripts/load-into-counting.py -x 1e8 -k 20 ecoli_reads-trim.kh ecoli_ref-5m.fastq.gz.abundtrim
~/khmer/khmer/scripts/abundance-dist.py -s ecoli_reads-trim.kh ecoli_ref-5m.fastq.gz.abundtrim ecoli_reads-trim.dist


