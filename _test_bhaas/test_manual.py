#!/usr/bin/env python3

import sys, os, re
sys.path.insert(0, "/Users/bhaas/GITHUB/genomeview.bhaas")
import genomeview

dataset_paths = ["data/pacbio.chr1.bam",
                 "data/illumina.chr1.bam"]
#,
#                 "/Users/nspies/Downloads/hg19.refseq.sorted.bed.gz"]
#reference = "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz"

#chrom = "chr1"
#start = 224368899
#end =   224398899

#doc = genomeview.visualize_data(dataset_paths, chrom, start, end, reference)

#genomeview.save(doc, "example.svg")


width=900
doc = genomeview.Document(width)

reference_path="ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz"
source = genomeview.FastaGenomeSource(reference_path)

chrom="chr1"
start=100
end=1000

view = genomeview.GenomeView(chrom, start, end, "+", source)
doc.add_view(view)

axis_track = genomeview.Axis("axis")
view.add_track(axis_track)

genomeview.save(doc, "example2.svg")

