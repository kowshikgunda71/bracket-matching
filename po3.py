# ________________________________________________________________________________________________________
# Team Identification Block
# Author 1:     Mr. Kowshik Gunda
# Student ID:   *20473953
# E-Mail:       kgunda@uco.edu
# Author 2:     Ms. Satya Danthuluri
# Student ID:   *20474582
# E-Mail:       sdanthuluri@uco.edu
# Course:       CMSC 5023 . Programming Languages
# CRN:          22058, Spring, 2019
#Project:      p03
# Due:          April 24, 2019
# Project Account Number: tt084
# ________________________________________________________________________________________________________
# -------------------------------------------------------------------------
# Includeing import statements here
# ---------------------------------------------------------------
from stack03 import balance
import sys
# -------------------------------------------------------------------------
# Main starts from here
# ---------------------------------------------------------------
if __name__ == '__main__':
    print("enter input file")
    f = open(sys.argv[1], "r")
    #f = open("test.dat"+".dat", "r")
    fi = open(sys.argv[2], "a+")

line = f.readline()
while line:
    print(balance(line))

    fi.write(line)
    fi.write(balance(line))
    line = f.readline()

f.close()
