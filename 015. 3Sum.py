#Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
class Solution(object):
    def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums=sorted(nums)
		i=0
		ans=[]
		while i<len(nums):
			j=i+1
			k=len(nums)-1
			while j<k:
				temp_sum=nums[i]+nums[j]+nums[k]
				if temp_sum<0:
					j+=1
				elif temp_sum>0:
					k-=1
				else:
					ans.append([nums[i],nums[j],nums[k]])
					j+=1
					while j<k and nums[j-1]==nums[j]:
						j+=1
			i+=1
			while i<len(nums) and nums[i-1]==nums[i]:
				i+=1
		return ans