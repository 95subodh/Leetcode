#Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
#
#Example 1:
#
#Input: k = 3, n = 7
#
#Output:
#
#[[1,2,4]]
#
#Example 2:
#
#Input: k = 3, n = 9
#
#Output:
#
#[[1,2,6], [1,3,5], [2,3,4]]

class Solution(object):
	def combinationSum3(self, k, n):
		"""
		:type k: int
		:type n: int
		:rtype: List[List[int]]
		"""
		ans=[]
		def sol(k,n,ind,lst):
			if k==0 and n==0:
				ans.append(lst)
			if k==0 or n==0:
				return
			for i in xrange(ind,10):
				sol(k-1, n-i, i+1, lst+[i])
		sol(k, n, 1, [])
		return ans