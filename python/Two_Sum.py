'''
Problem Statement:
Given a list of numbers and a number k, return two numbers from the list that add up to k.
If there are none such numbers, you can return False

Examples:
    Input: [10, 15, 3, 7], k=17
    Output: [10,7]

Author: 
https://www.github.com/ravikumark815

'''

import os
import time

def twoSum(li, k):
    for i, num1 in enumerate(li):
        for j, num2 in enumerate(li[i+1:]):
            if num1 + num2 == k:
                return [li[i], li[j+i+1]]
    return False

if __name__ == "__main__":
    print("\n~~~~~~~ Two Sum ~~~~~~~\n")
    
    li = []
    liStr = input("Enter the list of numbers separated by commas: ")
    liC = liStr.split(",")
    for i in liC:
        li.append(int(i))
    k = int(input("Enter the sum value: "))
    
    tstart = time.time()
    print("Result: ", twoSum(li, k))
    tend = time.time()

    print("\n~~~~~~~ Time Taken: ",(tend - tstart), "~~~~~~~\n")
