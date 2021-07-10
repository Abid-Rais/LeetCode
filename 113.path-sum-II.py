"""
113. Path Sum II 
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

from typing import List


class TreeNode:
    # Definition for a binary tree node.

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(currNode, currPath, currSum, allPaths):
            if not currNode:
                return []

            currSum += currNode.val
            if not currNode.left and not currNode.right and currSum == targetSum:
                allPaths.append(currPath + [currNode.val])
                return

            if currNode.left:
                dfs(currNode.left, currPath +
                    [currNode.val], currSum, allPaths)
            if currNode.right:
                dfs(currNode.right, currPath +
                    [currNode.val], currSum, allPaths)

        allPaths = []
        dfs(root, [], 0, allPaths)
        return allPaths
