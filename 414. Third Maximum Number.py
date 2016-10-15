#Given an array of integers, return the 3rd Maximum Number in this array, if it doesn't exist, return the Maximum Number. The time complexity must be O(n) or less.

class Solution(object):
	def thirdMax(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		a=b=c=-pow(10, 18)
		nums=set(nums)
		for i in nums:
			if i>=a:
				c,b,a=b,a,i
			elif i>=b:
				c,b=b,i
			elif i>=c:
				c=i
		return c if len(nums)>2 else max(nums)