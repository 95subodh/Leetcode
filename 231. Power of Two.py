#Given an integer, write a function to determine if it is a power of two.
class Solution(object):
    def isPowerOfTwo(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		return True if n^(n-1)==n+n-1 and n!=0 else False