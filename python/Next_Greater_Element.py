'''
Given an array A of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array. If no such element exists, output -1 

Input:
The first line of input contains a single integer T denoting the number of test cases.Then T test cases follow. Each test case consists of two lines. The first line contains an integer N denoting the size of the array. The Second line of each test case contains N space separated positive integers denoting the values/elements in the array A.

Output:
For each test case, print in a new line, the next greater element for each array element separated by space in order.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1018
Example:
Input
2
4
1 3 2 4
4
4 3 2 1
Output
3 4 4 -1
-1 -1 -1 -1

Author: https://github.com/ravikumark815
'''

def nextGreaterElement(nums):
    res = ""
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[j]>nums[i]:
                resTemp = nums[j]
                break
            resTemp = -1
        res = res + " " + str(resTemp)
    print(res)

if __name__=="__main__":
    li = []
    nums = []
    n = int(input("Enter the size of the array: "))
    liStr = input("Enter the elements separated by space: ")
    li = liStr.split(" ")
    for i in li:
        nums.append(int(i))
    nextGreaterElement(nums)