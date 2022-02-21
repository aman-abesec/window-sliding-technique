# ================================================================================
#                        1876. Substrings of Size Three with Distinct Characters
# ================================================================================
# A string is good if there are no repeated characters.
# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
# A substring is a contiguous sequence of characters in a string.
#
# Example 1:
# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
# The only good substring of length 3 is "xyz".
#
# Example 2:
# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        windowStart=0
        windowCount=0
        windowStr=""
        for windowEnd in range(len(s)):
            windowStr+=s[windowEnd]
            if(windowEnd+1>=3):
                if(windowStr[0]!=windowStr[1] and windowStr[1]!=windowStr[2] and windowStr[2]!=windowStr[0]):
                    windowCount+=1
                windowStr=windowStr[1:]
                windowStart+=1
        return windowCount
        
