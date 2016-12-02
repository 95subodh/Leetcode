# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

# For example, given the range [5, 7], you should return 4.

class Solution(object):
	def rangeBitwiseAnd(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		x=pow(2, 31)
		y=pow(2, 32)
		c=0
		while x:
			if x<=m and n<y:
				m-=x
				n-=x
				c+=x
			x/=2
			y/=2
		return c
