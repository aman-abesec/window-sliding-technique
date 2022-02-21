# ================================================================================
#                        1763. Longest Nice Substring
# ================================================================================
# A string s is nice if, for every letter of the alphabet that s contains, it appears both
#  in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear,
#   and 'B' and 'b' appear. However,
#  "abA" is not because 'b' appears, but 'B' does not.
# Given a string s, return the longest substring of s that is nice.
# If there are multiple, return the substring of the earliest occurrence. If there
# are none, return an empty string.
#
# Example 1:
# Input: s = "YazaAay"
# Output: "aAa"
# Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
# "aAa" is the longest nice substring.
#
# Example 2:
# Input: s = "Bb"
# Output: "Bb"
# Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
#
# Example 3:
# Input: s = "c"
# Output: ""
# Explanation: There are no nice substrings.

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        all_comb=[]
        for i in range(len(s)+1):
            for j in range(i):
                all_comb.append(s[j:i])
        result=[]
        result_index=[]
        for st in all_comb:
            for i in range(len(st)):
                if st[i].islower() and st[i].upper() not in st:
                    break
                elif st[i].isupper() and st[i].lower() not in st:
                    break
            else:
                result.append(st)
                result_index.append(len(st))
        if result==[]:
            return ""
        else:
            return result[result_index.index(max(result_index))]
