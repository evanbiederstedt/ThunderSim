# SVSimCmdOptions.java


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("help", metavar="h", description = "Print usage info")
parser.add_argument("Ploidy", metavar="p", description= "Specify the ploidy")
parser.add_argument("SV-rate", metavar="s", description= "Specify the rate of sv simulation")
parser.add_argument("TE-percent", metavar="e", description= "Specify the percent of TE induced SV")
parser.add_argument("Segment-mean-size", metavar="g", description= "Specify the mean size of the segments"")
parser.add_argument("Heter-Homo-ratio", metavar="z", description = "Ratio between Heterozygous and Homozygous", default=2.0)  # default?
parser.add_argument("tandem-dup-mean-size", metavar="d", description = "Mean times of tandem duplication")
parser.add_argument("max-tandemdup-size", metavar="x", description = "Specify max size of tandem duplications")
parser.add_argument("minimal-deletion-size", metavar="m", description = "Specify minimal size of deletions")
parser.add_argument("Copy-Neutral-LOH rate", metavar="l", description = "Specify Copy-Neutral LOH rate for deletions")
parser.add_argument("output-directory", metavar="o", description = "Specify the output directory, including vcf file and fasta file")
parser.add_argument("output-prefix", metavar="a", description = "Specify the output file prefix to discriminate each run")
parser.add_argument("clone-sv-number", metavar="c", description = "Specify sv numbers for each clone")
parser.add_argument("chromosome-length_file", metavar="v", description = "SSpecify the path and name for chromosome length file")
parser.add_argument("reference-sequence-file", metavar="n", description = "Specify the path and name for reference sequence file")
parser.add_argument("repeat-mask-file", metavar="k", description = "Specify the path and name for repeat mask file")
parser.add_argument("snv-indel-file", metavar="i", description = "SSpecify the path and name for snv-indel file")
args = parser.parse_args()

                    
                    
# CNVSegment.java
class CNVSegment(object):
    def __init__(self, chromosome, start, end, cnv)
        self.chromosome = chromosome
        self.start = start
        self.end = end
        self.cnv= cnv

# StructureVariant.java
class StructureVariant(object):
    def __init__(self, chromosome, sischrom, start, end, name, TE_induce, tepair, tebreakpoint, remnant, strand):
        
                 
