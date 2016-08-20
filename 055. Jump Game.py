#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
#Each element in the array represents your maximum jump length at that position.
#
#Determine if you are able to reach the last index.
class Solution(object):
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		mx=0
		for i in xrange(len(nums)):
			if mx>=i:
				mx=max(mx,nums[i]+i)
		return mx>=len(nums)-1