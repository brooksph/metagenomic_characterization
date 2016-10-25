Using the khmer recipes for characterization of metagenomic samples
===================================================================

Goal: To characterize metagenomic samples using khmer

Notes: For this I will use an e.coli metgenomic dataset provided by Sherine Awad 

----------------------------------------------------------------------------

Downloading khmer in a virualenv using git clone: 

-------------------------------------------------

mkdir khmer 
cd khmer 
conda create -n khmer python=2.7 anaconda

--------------------------------------------------

To generate a k-mer spectrum with from my genome using k=20: 

	~/khmer/khmer/scripts/load-into-counting.py -x 1e8 -k 20 reads.kh ../seqs/ecoli_ref-5m.fastq.gz

	~/khmer/khmer/scripts/abundance-dist.py -s reads.kh ../seqs/ecoli_ref-5m.fastq.gz reads.dist

To generate a read coverage spectrum execute the following command:

	~/khmer/khmer/sandbox/calc-median-distribution.py reads.kh ../seqs/ecoli_ref-5m.fastq.gz reads-cov.dist
	
Now lets grab the reads with coverage between 50 and 200x coverage and put them in reads-genome.fa

	~/khmer/khmer/sandbox/slice-reads-by-coverage.py reads.kh ../seqs/ecoli_ref-5m.fastq.gz reads-genome.fa -m 50 -M 200

Not lets grab all of the in abundance greater than 200 (i.e. repeats) and put them in reads-repeats.fa

	~/khmer/khmer/sandbox/slice-reads-by-coverage.py reads.kh ../seqs/ecoli_ref-5m.fastq.gz reads-repeats.fa -m 200