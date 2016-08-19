#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution.
class Solution(object):
    def twoSum(self, nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	dict={}
	for i in xrange(len(nums)):
		if (target-nums[i]) in dict:
			return [dict[target-nums[i]],i]
		dict[nums[i]]=i
