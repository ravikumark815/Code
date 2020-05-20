'''
Problem Statement:
Given a 32-bit signed integer, reverse digits of an integer.

Examples:
    Input: 123
    Output: 321

    Input: -123
    Output: -321

Author: 
https://www.github.com/ravikumark815

'''

import os
import time

def reverse(x):
    if(x==0):
        return 0
    if(x>0):
        x = int(str(x)[::-1])
    elif(x<0):
        a = str(x)[1:]
        x = -int(str(a)[::-1])

    neg_limit= -0x80000000
    pos_limit= 0x7fffffff

    if(x<0):
        val=x&neg_limit
        if(val==neg_limit):
            return x
        else:
            return 0
    else:
        val = x&pos_limit
        if(val==x):
            return x
        else:
            return 0

if __name__ == "__main__":
    print("\n~~~~~~~ Tower of Hanoi ~~~~~~~\n")
    
    x = int(input("Enter the number: "))
    
    tstart = time.time()
    print("Result: ", reverse(int(x)))
    tend = time.time()

    print("\n~~~~~~~ Time Taken: ",(tend - tstart), "~~~~~~~\n")
