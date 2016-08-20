#Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
class Solution(object):
	def integerBreak(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		l=[0,0,1,2,4,6,9]
		for i in xrange(7,n+1):
			m=0
			for j in xrange(2,i):
				m=max(j*l[i-j],m)
			l.append(m)
		return l[n]