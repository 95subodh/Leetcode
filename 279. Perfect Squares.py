#Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
#For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

class Solution(object):
	_dp = [0] 
	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		dp = self._dp
		while len(dp) <= n:
			dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
		return dp[n]
