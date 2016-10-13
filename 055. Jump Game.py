#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
#Each element in the array represents your maximum jump length at that position.
#
#Determine if you are able to reach the last index.
#
#For example:
#A = [2,3,1,1,4], return true.
#
#A = [3,2,1,0,4], return false.

class Solution(object):
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		update_list=[-1 for i in xrange(len(nums))]
		update_list[0]=0
		updated_ind=1
		for i in xrange(len(nums)):
			while updated_ind<len(nums) and updated_ind<=i+nums[i] and update_list[i]!=-1:
				update_list[updated_ind]=update_list[i]+1
				updated_ind+=1
		return True if update_list[-1]!=-1 else False