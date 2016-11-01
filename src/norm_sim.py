#!/usr/bin/python3



# SimulationParameters.java
class Simulation():
    def __init__(self, snv_rate = 0.001, indel_rate = 0.0003, transition_rate = 0.65, hetero_homo_ratio = 2.0, insert_percent = 0.5, indel_mean = 1.0, output_dir, chrlenpath, refpath, prefix="normal"):


# Picard: https://pypi.python.org/pypi/pyfaidx
# htslib/pysam


"""
    From README.pdf
    1.Parameters for normgenomsim_1.3.1.jar on germline SNV, INDEL simulation
    -o  output directory, string, required.
    -v  chromosome length file, string, required
    -n  reference sequence file, string, required
    -s  SNV rate, float number, default: 0.001
    -r  INDEL rate, float number, default: 0.0003
    -t  Transition/Transversion ratio, float number, default: 0.65
    -z  Heterozygous-Homozygous ratio, float number, default: 2.0
    -d  insertion percent to total INDELs, float number, default: 0.5
    -m  mean INDEL length, integer, default: 1
    -h  help, print this help message
    1
    -a  prefix, string, default: normal
"""


# SnvIndelSimCmdOp.java

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("help", metavar="h", description = "Print usage info")
parser.add_argument("SNV-rate", metavar="s", description = "Specify the rate of SNV simulation", default=0.001)
parser.add_argument("Indel-rate", metavar="r", description = "Specify the rate of indel simulation", default=0.0003)
parser.add_argument("Transition-percent", metavar="t", description = "Specify the transition mutation percent when snv simulation", default=0.65)
parser.add_argument("Heter-Homo-ratio", metavar="z", description = "Ratio between Heterozygous and Homozygous", default=2.0)
parser.add_argument("INS percent", metavar="d", description = "Specify the insertion percent, deletion percent is 1-insertion percent", default=0.5)
parser.add_argument("Indel-mean", metavar="m", description = "Specify the indel mean size", default=1)
parser.add_argument("output-directory", metavar="o", description = "Specify the output directory, including vcf file and fasta file")
parser.add_argument("input-directory", metavar="i", description = "Specify the input directory which contains reference sequence file and chromosome length file")
parser.add_argument("chromosome-length-file", metavar="v", description = "Specify the chromosome length file")
parser.add_argument("reference-file", metavar="n", description = "Specify the name and path of the reference sequence file")
parser.add_argument("file-prefix", metavar="a", description = "Specify the prefix for output file to differentiate each run")
args = parser.parse_args()

# InitializeChromLen.java

class InitalizeChromLen():
    chrLenArr = int(24)
    def generateChrLen()



# Genotype.java
# Enum for encapsulating a genotyp {homozygous, heterozygous}

from enum import Enum
class Genotype(Enum):
    HOMO = "M"
    HETERO = "R"

# SisterChrom.java
# Enum for encapsulating a chromatin{chromatinA, chromatinB}

from enum import Enum
class SisterChrom(Enum):
    CHMTIN_A = "A"
    CHMTIN_B = "B"
    CHMTIN_C = "C"
    CHMTIN_D = "D"
    CHMTIN_E = "E"
    CHMTIN_F = "F"
