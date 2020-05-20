'''
Problem Statement:
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

Examples:
    Input: [1,2,3,4,5]
    Output: [120,60,40,30,24]

    Input: [3,2,1]
    Output: [2,3,6]

Author: 
https://www.github.com/ravikumark815

'''

import os
import time
from functools import reduce

def productArray(li):
    res = []
    prod = reduce((lambda x, y: x * y), li)
    
    for i in li:
        res.append(prod//i)
    
    return res

if __name__ == "__main__":
    print("\n~~~~~~~ Product Array ~~~~~~~\n")
    
    li = []
    liStr = input("Enter the list of numbers separated by commas: ")
    liC = liStr.split(",")
    for i in liC:
        li.append(int(i))
    
    tstart = time.time()
    print("Result: ", productArray(li))
    tend = time.time()

    print("\n~~~~~~~ Time Taken: ",(tend - tstart), "~~~~~~~\n")
