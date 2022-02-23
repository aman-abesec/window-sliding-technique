# ================================================================================
#                        209. Minimum Size Subarray Sum
# ================================================================================
# Given an array of positive integers nums and a positive integer target, return the minimal
# length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is
# greater than or equal to target. If there is no such subarray, return 0 instead.
#
# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
#
# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
# Constraints:
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_start=0
        count=math.inf
        window_sum=0
        for window_end in range(len(nums)):
            window_sum+=nums[window_end]
            while(window_sum>=target):
                if(window_sum>=target):
                    count=min(count,window_end-window_start+1)
                window_sum-=nums[window_start]
                window_start+=1
        # print(window_sum)
        if count==math.inf :return 0
        return count

            
