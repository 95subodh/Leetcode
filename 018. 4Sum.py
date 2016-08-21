#Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

import itertools
class Solution(object):
    def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		nums=sorted(nums)
		ans=[]
		for i in xrange(len(nums)):
			for j in xrange(i+1,len(nums)):
				k=j+1
				l=len(nums)-1
				while k<l:
					t=nums[i]+nums[j]+nums[k]+nums[l]
					if t<target:
						k+=1
					elif t>target:
						l-=1
					else:
						ans.append([nums[i],nums[j],nums[k],nums[l]])
						k+=1
		ans.sort()
		return list(ans for ans,_ in itertools.groupby(ans))