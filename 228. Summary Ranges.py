#Given a sorted integer array without duplicates, return the summary of its ranges.
#
#For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

class Solution(object):
	def summaryRanges(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		l=[]
		s=""
		if nums:
			s=str(nums[0])
		i=0
		while i<len(nums):
			j=i+1
			while j<len(nums) and nums[j]==nums[j-1]+1:
				j+=1
			if i!=j-1:
				s+='->'+str(nums[j-1])
			i=j
			l.append(s)
			s=""
			if i<len(nums):
				s=str(nums[i])
		if s:
			l.append(s)
		return l