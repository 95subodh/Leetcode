#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
class Solution(object):
    def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		return len(nums)*(len(nums)+1)/2-sum(nums)