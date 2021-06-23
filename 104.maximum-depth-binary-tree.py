"""
    104. Maximum Depth of Binary Tree
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

    Example 2:
    Input: root = [1,null,2]
    Output: 2

    Example 3:
    Input: root = []
    Output: 0

    Example 4:
    Input: root = [0]
    Output: 1

    Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
"""

from collections import deque


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Recrusive Depth-First Search 
        T(n) = O(n)
            Go through all nodes 
        S(n) = O(n)
            Recursive call stack can be as big as many nodes there are 
        """
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth(self, root: TreeNode) -> int:
        """
            Iterative Breadth-First Search
            T(n) = O(n)
                Go through all nodes 
            S(n) = O(n)
                Queue can be as big as many nodes there are 
        """
        if not root:
            return 0

        maxDepth = 0
        queue = deque()
        queue.append(root)
        while queue:
            maxDepth += 1
            for _ in range(len(queue)):
                currNode = queue.popleft()
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
        return maxDepth
