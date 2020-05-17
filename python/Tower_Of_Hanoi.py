'''
Problem Statement:
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
1) Only one disk can be moved at a time.
2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
3) No disk may be placed on top of a smaller disk.

Approach:
Take an example for 2 disks :
Let rod 1 = 'A', rod 2 = 'B', rod 3 = 'C'.

Step 1 : Shift first disk from 'A' to 'B'.
Step 2 : Shift second disk from 'A' to 'C'.
Step 3 : Shift first disk from 'B' to 'C'.

The pattern here is :
Shift 'n-1' disks from 'A' to 'B'.
Shift last disk from 'A' to 'C'.
Shift 'n-1' disks from 'B' to 'C'.

Example:
Input : 2
Output : Disk 1 moved from A to B
         Disk 2 moved from A to C
         Disk 1 moved from B to C

Time Complexity: O(2^n)
Space Complexity: O(n)

Author: 
https://www.github.com/ravikumark815

'''

import os
import time

def towerOfHanoi(n , from_rod, aux_rod, to_rod): 
    if n == 1: 
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    towerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    towerOfHanoi(n-1, aux_rod, to_rod, from_rod)

if __name__ == "__main__":
    print("\n~~~~~~~ Tower of Hanoi ~~~~~~~\n")
    
    n = int(input("Enter the number of Disc: "))
    
    tstart = time.time()
    towerOfHanoi(n, 'A', 'B', 'C')
    tend = time.time()

    print("\n~~~~~~~ Time Taken: ",(tend - tstart), "~~~~~~~\n")
