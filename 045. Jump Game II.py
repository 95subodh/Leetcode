#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
#Each element in the array represents your maximum jump length at that position.
#
#Your goal is to reach the last index in the minimum number of jumps.
#
#For example:
#Given array A = [2,3,1,1,4]
#
#The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#
#Note:
#You can assume that you can always reach the last index.

class Solution(object):
	def jump(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		update_list=[-1 for i in xrange(len(nums))]
		update_list[0]=0
		updated_ind=1
		for i in xrange(len(nums)):
			while updated_ind<len(nums) and updated_ind<=i+nums[i]:
				update_list[updated_ind]=update_list[i]+1
				updated_ind+=1
		return update_list[-1]