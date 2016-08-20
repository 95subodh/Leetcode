#Given an integer n, return the number of trailing zeroes in n!.
#
#Note: Your solution should be in logarithmic time complexity.
class Solution(object):
    def trailingZeroes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		ans=0
		div=5
		while n>=div:
			ans+=n/div
			div*=5
		return ans