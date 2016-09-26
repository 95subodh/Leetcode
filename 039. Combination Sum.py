#Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
#The same repeated number may be chosen from C unlimited number of times.
#
#Note:
#All numbers (including target) will be positive integers.
#The solution set must not contain duplicate combinations.
#For example, given candidate set [2, 3, 6, 7] and target 7, 
#A solution set is: 
#[
#	[7],
#	[2, 2, 3]
#]

class Solution(object):
	def combinationSum(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		ans=[]
		def sol(choose,remain_number,last_inserted):
			if remain_number==0:
				ans.append(choose)
			for i in candidates:
				if i<=remain_number and i>=last_inserted:
					sol(choose+[i], remain_number-i, i)
		sol([], target)
		return ans