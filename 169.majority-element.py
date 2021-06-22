"""
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

    Example 1:
    Input: nums = [3,2,3]
    Output: 3

    Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
    
    Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -231 <= nums[i] <= 231 - 1
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
            T(n) = O(n)
                Iterate through nums
            S(n) = O(n)
                Keep track of all frequencies of numbers 
        """
        elemCount = {}
        currMajor = nums[0]
        for num in nums:
            elemCount[num] = elemCount.get(num, 0) + 1
            if elemCount[num] > elemCount[currMajor]:
                currMajor = num
        return currMajor
