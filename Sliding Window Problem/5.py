# ================================================================================
#                        3. Longest Substring Without Repeating Characters
# ================================================================================
# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start=0
        window_count=0
        hash_map={}
        for window_end in range(len(s)):
            curr_char=s[window_end]
            hash_map[curr_char]=hash_map.get(curr_char,0)+1
            if(len(hash_map)==(window_end-window_start)+1):
                window_count=max(window_count,(window_end-window_start)+1)
            while(len(hash_map)!=(window_end-window_start)+1):
                hash_map[s[window_start]]-=1
                if hash_map[s[window_start]]==0:
                    del hash_map[s[window_start]]
                window_start+=1
        # print(hash_map)
        return window_count
