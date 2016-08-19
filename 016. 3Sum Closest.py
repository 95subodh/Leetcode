#Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
class Solution(object):
    def threeSumClosest(self, nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	nums=sorted(nums)
	i=ans=0
	mi=pow(10, 18)
	while i<len(nums):
		j=i+1
		k=len(nums)-1
		while j<k:
			temp_sum=nums[i]+nums[j]+nums[k]
			if mi>abs(target-temp_sum):
				mi=abs(target-temp_sum)
				ans=temp_sum
			if temp_sum<target:
				j+=1
			elif temp_sum>target:
				k-=1
			else:
				break
		i+=1
	return ans
