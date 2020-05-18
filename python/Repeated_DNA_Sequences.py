'''
Problem Statement:
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]

Author: 
https://www.github.com/ravikumark815

'''

import os
import time
import collections

def findRepeatedDnaSequences(s):
	counter = collections.Counter(s[i:i+10] for i in range(len(s)-9))
	return [s for s in counter if counter[s] > 1]

if __name__ == "__main__":
    print("\n~~~~~~~ Repeated DNA Sequences ~~~~~~~\n")
    
    s = input("Enter the DNA Sequence: ")
    
    tstart = time.time()
    print("\nResult: ", findRepeatedDnaSequences(s))
    tend = time.time()

    print("\n~~~~~~~ Time Taken: ",(tend - tstart), "~~~~~~~\n")