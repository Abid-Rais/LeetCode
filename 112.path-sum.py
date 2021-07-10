"""
112. Path Sum 
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:
Input: root = [1,2], targetSum = 0
Output: false
 
Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

from collections import deque


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """
        DFS Recursive
        T(n) = O(n)
            Iterate through all nodes 
        S(n) = O(n)
            Iterate through all nodes
        """
        if not root:
            return False

        if not root.left and not root.right and targetSum - root.val == 0:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """
        DFS Iterative
        T(n) = O(n)
            DFS through all nodes 
        S(n) = O(n)
            Stack 
        """
        if not root:
            return False

        stack = deque()
        stack.append((root, 0))
        while stack:
            currNode, currSum = stack.pop()
            currSum += currNode.val
            if not currNode.left and not currNode.right and currSum == targetSum:
                return True
            if currNode.left:
                stack.append((currNode.left, currSum))
            if currNode.right:
                stack.append((currNode.right, currSum))
        return False
