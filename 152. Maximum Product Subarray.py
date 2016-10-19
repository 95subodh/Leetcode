#Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
#For example, given the array [2,3,-2,4],
#the contiguous subarray [2,3] has the largest product = 6.

class Solution(object):
	def maxProduct(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		def sol(num):
			if len(num)==0:
				return -pow(10, 18)
			s=1
			for i in num:
				s*=i
			if s>0 or len(num)==1:
				return s
			else:
				s1=s2=s
				for i in num:
					s1/=i
					if i<0:
						break
				for i in num[::-1]:
					s2/=i
					if i<0:
						break
				return max(s1,s2)
		k=-1
		mx=-pow(10, 18)
		for i in xrange(len(nums)):
			z=mx
			if nums[i]==0:
				z=max(sol(nums[k+1:i]),0)
				k=i
			elif i==len(nums)-1:
				z=sol(nums[k+1:i+1])
			mx=max(mx,z)
		return mx