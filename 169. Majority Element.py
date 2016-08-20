#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
#You may assume that the array is non-empty and the majority element always exist in the array.
class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		
		#Moore's Voting Algorithm
		
		majority=0
		count =0
		for i in xrange(len(nums)):
			if nums[i]==nums[majority]:
				count+=1
			else:
				count-=1
			if count==0:
				majority=i
				count=1
		return nums[majority]