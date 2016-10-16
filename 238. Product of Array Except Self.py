#Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
#Solve it without division and in O(n).
#
#For example, given [1,2,3,4], return [24,12,8,6].
#
#Follow up:
#Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution(object):
	def productExceptSelf(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		ll, rl, ans, c=[1], [1], [], 0
		for i in nums:
			if i==0:
				c+=1
			ll.append(ll[-1]*i)
			
		for i in nums[::-1]:
			rl.append(rl[-1]*i)
			
		for i in xrange(len(nums)):
			if c>1 or (c==1 and nums[i]):
				ans.append(0)
			else:
				ans.append(ll[i]*rl[len(nums)-i-1])
		return ans