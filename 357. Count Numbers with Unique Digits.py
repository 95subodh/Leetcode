#Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
#
#Example:
#Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

class Solution(object):
	def countNumbersWithUniqueDigits(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		l=[1,10]
		x=9
		for i in xrange(n):
			x*=(9-i)
			l.append(l[-1]+x)
		return l[n]