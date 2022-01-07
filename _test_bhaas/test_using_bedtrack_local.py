#!/usr/bin/env python3

import sys, os, re
sys.path.insert(0, "/Users/bhaas/GITHUB/genomeview.bhaas")

import genomeview.genomeview
import genomeview.axis

#from genomeview.genomeview import *
#from genomeview.axis import *
#from genomeview.track import *
#from genomeview.bamtrack import *
from genomeview.bedtrack import BEDTrack
#from genomeview.graphtrack import *
from genomeview.intervaltrack import *
from genomeview.genomesource import *

#from genomeview.export import render_to_file, save

#from genomeview.convenience import visualize_data
#from genomeview.utilities import get_one_track


class MyTrack(IntervalTrack):

    def __init__(self, name=None):
        """
        Args:
            name (str): name of the track
            bed_path (str): path of the bed file to display

        """
        super().__init__([], name=name)
        
        #self.bed_path = bed_path
        self.intervals = self

        self.draw_locus_labels = True
        self.include_locus_fn = None

        self.row_height = 12
        self.thick_width = self.row_height
        self.thin_width = 5
        self.thinnest_width = 1

        self.min_exon_width = 1


    def draw_interval(self, renderer, interval):
        yield from super().draw_interval(renderer, interval)
        return

    def __iter__(self):
        interval = Interval("my1", "chr1", 200, 300, '+')
        yield interval


        interval = Interval("my2", "chr1", 600, 800, '-')
        yield interval

        return





def main():

    #dataset_paths = ["data/pacbio.chr1.bam",
    #                 "data/illumina.chr1.bam"]
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

    reference_path="/Users/bhaas/DB/CTAT_GENOME_LIB/GRCh38_gencode_v22_CTAT_lib_Oct012019.plug-n-play/ctat_genome_lib_build_dir/ref_genome.fa"
    source = FastaGenomeSource(reference_path)

    """
    chrom="chr1"
    start=100
    end=1000
    """

    chrom="chr8"
    start=127000000
    end=129000000
    
    view = genomeview.GenomeView(chrom, start, end, "+", source)
    doc.add_view(view)


    """
    mytrack = MyTrack()
    view.add_track(mytrack)
    """
    
    axis_track = genomeview.Axis("axis")
    view.add_track(axis_track)

    
    bed_file = "/Users/bhaas/DB/CTAT_GENOME_LIB/GRCh38_gencode_v22_CTAT_lib_Oct012019.plug-n-play/ctat_genome_lib_build_dir/ref_annot.bed"
    bed_track = genomeview.BEDTrack(bed_file, name="GRCh38-gencode_v22")
    bed_track.draw_locus_labels = False
    
    view.add_track(bed_track)

    
    genomeview.save(doc, "example3.svg")

if __name__=='__main__':
    main()





