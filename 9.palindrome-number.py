"""
    9. Palindrome Number 
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

    Example 1:
    Input: x = 121
    Output: true

    Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    
    Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    
    Example 4:
    Input: x = -101
    Output: false
    
    Constraints:
    -231 <= x <= 231 - 1
    
    Follow up: Could you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
            T(n) = O(n)
            S(n) = O(n) 
                Converting int to str takes constant space 
            This method does not comply with follow-up 
        """

        if x < 0:
            return False

        x = str(x)
        left = 0
        right = len(x) - 1
        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1

        return True

    def isPalindrome(self, x: int) -> bool:
        """
            T(n) = O()
            S(n) = O(1)
        """
        if (x < 0) or (x != 0 and x % 10 == 0):
            return False

        reverse = 0
        while x > reverse:
            pass

        return True
