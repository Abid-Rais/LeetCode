"""
83. Remove Duplicates from Sorted List 
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
 
Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
            T(n) = O(n)
                Iterate through all nodes 
            S(n) = O(1)
        """
        if not head:
            return None

        currNode = nextNode = head
        while currNode:
            if nextNode and currNode.val == nextNode.val:
                nextNode = nextNode.next
            else:
                currNode.next = nextNode
                currNode = currNode.next
                nextNode = currNode
        return head
