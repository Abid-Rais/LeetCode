"""
    20. Valid Parentheses
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    
    Example 1:
    Input: s = "()"
    Output: true

    Example 2:
    Input: s = "()[]{}"
    Output: true

    Example 3:
    Input: s = "(]"
    Output: false

    Example 4:
    Input: s = "([)]"
    Output: false

    Example 5:
    Input: s = "{[]}"
    Output: true
    
    Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        """
            T(n) = O(n)
                Iterate through all chars in input 
            S(n) = O(n)
                Extra space needed for stack 
        """
        paren = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = deque()
        for char in s:
            if char in paren.keys():
                if stack and paren[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
