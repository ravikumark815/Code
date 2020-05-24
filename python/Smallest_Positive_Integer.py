'''
Problem Statement:
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

Examples:
    Input: [3, 4, -1, 1]
    Output: 2

    Input: [1,2,0]
    Output: 3

Author: 
https://www.github.com/ravikumark815

'''

import os
import time
from functools import reduce

def smallestPositiveInteger(nums):
    N = len(nums)
    nums = [0]+nums
    for i, num in enumerate(nums):
        if num == i:
            continue
        index = num
        nums[i] = 0
        while 0< index <= N and nums[index] != index:
            tmp = nums[index]
            nums[index] = index
            index = tmp
    i = 1
    while i <= N:
        if nums[i] == 0:
            return i
        i += 1
    return N+1

if __name__ == "__main__":
    print("\n~~~~~~~ Smallest Positive Integer ~~~~~~~\n")
    
    li = []
    liStr = input("Enter the list of numbers separated by commas: ")
    liC = liStr.split(",")
    for i in liC:
        li.append(int(i))
    
    tstart = time.time()
    print("Result: ", smallestPositiveInteger(li))
    tend = time.time()

    print("\n~~~~~~~ Time Taken: ",(tend - tstart), "~~~~~~~\n")
