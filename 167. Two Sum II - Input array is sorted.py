#Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
class Solution(object):
	def twoSum(self, numbers, target):
		"""
		:type numbers: List[int]
		:type target: int
		:rtype: List[int]
		"""
		i=0
		j=len(numbers)-1
		while i<j:
			if numbers[i]+numbers[j]<target:
				i+=1
			elif numbers[i]+numbers[j]>target:
				j-=1
			else:
				return [i+1,j+1]