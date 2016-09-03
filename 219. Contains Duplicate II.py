#Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		dict = {}
		for i in xrange(len(nums)):
			if nums[i] in dict:
				if i - dict[nums[i]] <= k:
					return True
				dict[nums[i]]=i
			else:
				dict[nums[i]]=i	
		return False