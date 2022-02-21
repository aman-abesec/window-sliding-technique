#==========================================================================
#                        219. Contains Duplicate II
#==========================================================================
# Given an integer array nums and an integer k, return true if
# there are two distinct indices i and j in the array such that
# nums[i] == nums[j] and abs(i - j) <= k.
#
# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

#==============================Method-1 in Python========================
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for windowStart in range(len(nums)):
            windowEnd=windowStart+1
            while(abs(windowStart-windowEnd)<=k and windowEnd<len(nums)):
                if(nums[windowStart]==nums[windowEnd]):
                    return True
                windowEnd+=1
        return  False

#=============================Method-2 in Python===================================
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map=dict()
        for i in range(len(nums)):
            curr=nums[i]
            if(curr in hash_map and abs(hash_map[curr]-i)<=k):
                return True
            hash_map[curr]=i
        return False
