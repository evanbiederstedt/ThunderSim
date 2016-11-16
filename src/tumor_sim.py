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
        sistchr = Converter.getSisterChromFromIndex(sisidx)
        #variant = StructureVariant()
        if svtype == 0:
            #variant = TandemDup()
            variant.sischrom = sistchr
            variant.name = "TandemDup"
            # determine duplication times
            duptimes = np.random.exponential(1) + 1;
            # ((TandemDup)variant).setDuptimes(duptimes)
            elif svtype == 1:
            # deletion
            # variant = Deletion()
            # variant.end = site + random.nextInt(seg) + 1;
            variant.name = "Deletion"
            # Determine two or one copy loss , Hetero/Homo = hethomratio (only for the first run)
            if (run == 0 and copy > (1 / (hethomratio + 1)) * hethomratio):
                
                    
    @classmethod
    def determineSisterChrom(cls, ploidy):
        sischrIndex = np.random.randint(ploidy)
        sistchr = None
        if sischrIndex==0:
            sistchr = SisterChrom.CHMTIN_A
        elif sischrIndex==1:
            sistchr = SisterChrom.CHMITN_B
        elif sischrIndex==2:
            sistchr = SisterChrom.CHMITN_C
        elif sischrIndex==3:
            sistchr = SisterChrom.CHMITN_D
        elif sischrIndex==4:
            sistchr = SisterChrom.CHMITN_E
        elif sischrIndex==5:
            sistchr = SisterChrom.CHMITN_F
        else:
            print("invalid ploidy. Ploidy should not be greater than 6!!")
            System.exit(0)
        return sistchr
                    
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

                    
class Convert(object):
    @classmethod
    def getSisterChromIndex(cls, eventChr):
        eventChrIndex = 0
        if eventChr==CHMTIN_A:
            eventChrIndex = 0
        elif eventChr==CHMITN_B:
            eventChrIndex = 1
        elif eventChr==CHMITN_C:
            eventChrIndex = 2
        elif eventChr==CHMITN_D:
            eventChrIndex = 3
        elif eventChr==CHMITN_E:
            eventChrIndex = 4
        elif eventChr==CHMITN_F:
            eventChrIndex = 5
        else:
            print("invalid chromosome")
        return eventChrIndex

                    
    @classmethod
    def convertChrid(cls, cid, startbase, chrnum):
        # cid is what?
        if startbase == 0:
            chrid = cid + 1
        else:
            chird = cid
        if chrid = chrnum - 1:
            chr = "X"
        elif chrid = chrnum:
            chr = "Y"
        else:
            chr = str(chrid)
        return chr
                    
    @classmethod
    def selectChrom(cls, chrnum):
        chridx = np.random.randint(chrnum) + 1
        if chridx == chrnum -1:
            chrid = "X"
        elif chridx == chrnum:
            chrid = "Y"
        else:
            chrid = str(chridx)
        return chrid
             
    @classmethod
    def getSisterChromFromIndex(cls, index):
        srcChr = None
        # get the sister chrom from the index
        if index==0:
           srcChr = SisterChrom.CHMTIN_A
        elif index==1:
            srcChr = SisterChrom.CHMITN_B
        elif index==2:
            srcChr = SisterChrom.CHMITN_C
        elif index==3:
            srcChr = SisterChrom.CHMITN_D
        elif index==4:
            srcChr = SisterChrom.CHMITN_E
        elif index==5:
            srcChr = SisterChrom.CHMITN_F
        else:
            print("invalid chromosome index in ParameterizedSimulator!!")
        return srcChr
                    
                    
# 	 * convert vcf snv record to snv
                    
    @classmethod
    def convertVCFtoSNV(cls, vcfrecord):
        fields = vcfrecord.split("\t") # this probably doesn't work
        pos = Integer.parseInt(fields[1])
        ref = fields[3]
        alt = fields[4]
                    # chromtin = SisterChrom()
                    # gt = Genotype()
        genotype = fields[9]
        if genotype == "0|1":
            chromtin = SisterChrom.CHMITN_B
            gt = Genotype.HETERO
        elif genotype == "1|0":
            chromtin = SisterChrom.CHMTIN_A
            gt = Genotype.HETERO
        else:
            chromtin = None
            gt = Genotype.HOMO
                    # snv = MutRec()
        snv.pos = pos
        snv.ref = ref
        snv.alt = alt
        snv.sisChrom = chromtin
        snv.gentype = gt
        return snv
                    

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
