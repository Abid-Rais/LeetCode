"""
    Given the root of a binary tree, invert the tree, and return its root.

    Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

    Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]

    Example 3:
    Input: root = []
    Output: []
"""

from collections import deque


class TreeNode:
    # Definition for a binary tree node.

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
            Recursive
            T(n) = O(n)
                Have to iterate through all nodes
            S(n) = O(n)
                Recursive call stack is as big as many nodes there are 
        """
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
            Iterative
            T(n) = O(n)
                Have to iterate through all nodes
            S(n) = O(n)
                Queue can be as long as many nodes there are 
        """
        if not root:
            return None

        queue = deque()
        queue.append(root)
        while queue:
            curr = queue.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return root
