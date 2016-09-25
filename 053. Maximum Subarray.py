# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
class Solution(object):
    def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		mx=tm=nums[0]
		for i in nums[1:]:
			tm=max(i,tm+i)
			mx=max(tm,mx)
		return mx
