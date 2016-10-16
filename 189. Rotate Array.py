#Rotate an array of n elements to the right by k steps.
#
#For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
#Note:
#Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

class Solution(object):
	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		def reverse(nums, start, end):
			while start < end:
				nums[start], nums[end-1] = nums[end-1], nums[start]
				start += 1
				end -= 1
		k %= len(nums)
		reverse(nums, 0, len(nums))
		reverse(nums, 0, k)
		reverse(nums, k, len(nums))