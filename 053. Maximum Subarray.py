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