# ==========================================================================
#                        643. Maximum Average Subarray I
# ==========================================================================
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum
# average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
#
# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#
# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000

import math
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg=-(math.inf)
        windowStart=0
        windowSum=0
        for windowEnd in range(len(nums)):
            windowSum+=nums[windowEnd]
            if(k<=windowEnd+1):
                maxAvg=max(maxAvg,windowSum)
                windowSum-=nums[windowStart]
                windowStart+=1
        return maxAvg/k
