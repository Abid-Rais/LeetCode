"""
    94. Binary Tree Inorder Traversal 
    Given the root of a binary tree, return the inorder traversal of its nodes' values.

    Example 1:
    Input: root = [1,null,2,3]
    Output: [1,3,2]

    Example 2:
    Input: root = []
    Output: []

    Example 3:
    Input: root = [1]
    Output: [1]

    Example 4:
    Input: root = [1,2]
    Output: [2,1]

    Example 5:
    Input: root = [1,null,2]
    Output: [1,2]
    
    Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
    
    Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import List
from collections import deque


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Recursive 
        T(n) = O(n)
            Iterate through all nodes 
        S(n) = O(n)
            Recursive call stack is as big as many nodes there are
            Worst case is all nodes chain in one direction
        """
        if not root:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Iterative
        T(n) = O(n)
            Iterate through all nodes 
        S(n) = O(n)
            Stack can be as long as many nodes there are 
            Worst case is if all nodes chain to the left 
        """
        if not root:
            return []

        res = []
        stack = deque()
        currNode = root
        while stack or currNode:
            while currNode:
                stack.append(currNode)
                currNode = currNode.left

            currNode = stack.pop()
            res.append(currNode.val)
            currNode = currNode.right

        return res
