#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
class Solution(object):
    def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		i=j=0
		while i<len(nums):
			if nums[i]!=0:
				nums[j]=nums[i]
				if i!=j:nums[i]=0
				j+=1
			i+=1