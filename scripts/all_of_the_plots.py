Plot 
----
#Extract reads by coverage 
./plot-abundance-dist.py ecoli_reads.dist ecoli_reads-dist.png --ymax=300

#Estimate saturation of sequencing

./plot-saturation-curve.py saturation_report.txt saturation.png --xmin 0 --ymin 0 --xmax 1500

#Error-trim reads

./plot-abundance-dist.py ecoli_reads-trim.dist reads-trim-dist.png --xmax=20 --ymax=90000

#Trim metagenome and transcriptome reads with variable coverage k-mer trimming
./plot-abundance-dist.py reads-trim.dist reads-trim-dist.png --xmax=20 --ymax=18000
