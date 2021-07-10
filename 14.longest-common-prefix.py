"""
    14. Longest Common Prefix 
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

    Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
    
    Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
            T(n) = O(S) where S is the total number of characters in the input 
            S(n) = O(1)
        """
        prefix = ""
        strs = sorted(strs, key=lambda word: len(word))
        firstWord = strs[0]
        for i in range(len(firstWord)):
            for j in range(1, len(strs)):
                if (len(strs[j]) > i) and strs[j][i] != firstWord[i]:
                    return prefix
            prefix += firstWord[i]

        return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
            T(n) = O(S)
            S(n) = O(1)
            Same idea as above but this time sort list lexographically and only compare 
            first and last word as those two words will be the most distinct. 
        """
        prefix = ""
        strs = sorted(strs)
        firstWord = strs[0]
        lastWord = strs[-1]
        for i in range(len(firstWord)):
            if (len(lastWord) > i) and firstWord[i] != lastWord[i]:
                return prefix
            prefix += firstWord[i]
        return prefix
