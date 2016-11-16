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
        

# LargeSegment.java


# TandemDup.java
class TandemDup(StructureVariant):
                    

# Translocation.java

class Translocation(object):
    def __init__(self, chr1, chr2, brkpt1, brkpt2, bal, name):
        self.chr1 = chr1
        self.chr2 = chr2
        self.brkpt1 = brkpt1
        self.brkpt2 = brkpt2
        self.bal = bal
        self.name = name
                    
    def stringify(self):
        return chr1 + "\t" + brkpt1 + "\t" + chr2 + "\t" + brkpt2 + "\t" + name + "\n"
                
# SimulateRegularSV.java
                    
class SimulateRegularSV(object):
                    
    @classmethod
    def constructRegulatVariant(cls, anchorChr, chr, sisidx, segmentidx, start, end, parameter, run, seghash, chrnum):
        homonum = seghash.get(chr).size()  # what is this? seghash.get()?
        meanTdtime = parameter.ploidity
        maxTdsize = parameter.maxtdsize
        minDelsize = parameter.mindelsize
        hethomratio = parameter.heterhomoratio
        copyneutralLOHrate = parameter.copyneutral_LOH_rate
        expGen = np.random.exponential(1/meanTdtime)
        # 0: tandemDup
        # 1: deletion
        # 2: inversion(no CN change)
        # 3: insertion (same or different chromosome, cut or copy paste)
        svtype = np.random.randint(4)
        segmentLen = end - start
        if segmentLen > maxTdsize:
            while svtype == 0:
                svtype = np.random.randint(4)
        elif segmentLen < minDelsize:
            while svtype == 1:
                svtype = np.random.randint(4)
        print("Start simulating a regular SV, svtype is " + svtype)
                    
                    
                    
# Converter.java
                    
import main_simulator
import genotype
import mutrec
import sisterchrom
import d_chr_insertion
import deletion
import s_chr_insertion
import seq_source
import strand
import structure_variant
import tandem_dup
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
