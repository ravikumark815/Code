'''
Problem Statement:
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Let the marker for NULL pointers be '#'

Approach:
Basically we could easily recreate the tree from a BFS array by tracking the position of the children in the array for any element as :

current position in the BFS array + (current position+1) == left child
current position in the BFS array + (current position+2) == right child
Recur down building the array in a top down manner
e.g:

    1
   / \
  2   3
     / \
    4   5
as
[1,2,3,null, null, 4, 5]

Notice the array from leetcode:
Position 0, our root has left and right children as index 1,2
Position 1 child has left and right children as indices: 1+(1+1) = 3, 1+(1+2) = 4
Position 2 chid has left and right children as indices: 2+(2+1) = 5, 2+(2+2) = 6

Examples:
    Input:
        12
        /
    13
    Output: 12 13 -1 -1 -1

    Input:
      20
    /   \
   8     22 
    Output: 20 8 -1 -1 22 -1 -1
    
    Input:
         20
       /    
      8     
     / \
    4  12 
      /  \
     10  14
    Output: 20 8 4 -1 -1 12 10 -1 -1 14 -1 -1 -1 

Author: 
https://www.github.com/ravikumark815

'''

import os
import time
import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def buildNode(self, val):
        return None if val == '#' else TreeNode(int(val))

    def serialize(self, root):
        queue = [root]
        for node in queue:
            if not node:
                continue
            queue += [node.left, node.right]

        return ':'.join(
            map(lambda item: str(item.val) if item else '#', queue))

    def deserialize(self, data):
        parts = data.split(':')
        root = self.buildNode(parts[0])
        queue, i = collections.deque([root]), 1

        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = map(
                    self.buildNode, (parts[i], parts[i + 1]))
                queue.append(node.left)
                queue.append(node.right)
                i += 2
        return root

if __name__ == "__main__":
    print("\n~~~~~~~ Serialize and Deserialize a Binary Tree ~~~~~~~\n")
    
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)

    a.left = b
    a.right = c
    c.left = d
    c.right = e

    tstart = time.time()
    codec = Codec()
    s = codec.serialize(a)
    print(s)
    root = codec.deserialize(s)
    print(codec.serialize(root))    
    tend = time.time()

    print("\n~~~~~~~ Time Taken: ",(tend - tstart), "~~~~~~~\n")
