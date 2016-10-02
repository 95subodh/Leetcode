#Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
#Each number in C may only be used once in the combination.
#
#Note:
#All numbers (including target) will be positive integers.
#The solution set must not contain duplicate combinations.
#For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
#A solution set is: 
#[
#	[1, 7],
#	[1, 2, 5],
#	[2, 6],
#	[1, 1, 6]
#]

class Solution(object):
	def combinationSum2(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		ans=[]
		candidates=sorted(candidates)
		print candidates
		def sol(choose,remain_number,last_pos_inserted):
			if remain_number==0:
				ans.append(choose)
			for i in xrange(last_pos_inserted+1,len(candidates)):
				if candidates[i]<=remain_number and (last_pos_inserted==i-1 or candidates[i-1]!=candidates[i]):
					sol(choose+[candidates[i]], remain_number-candidates[i], i)
		sol([],target, -1)
		return ans