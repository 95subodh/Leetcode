#Given a positive integer, return its corresponding column title as appear in an Excel sheet.
class Solution(object):
	def convertToTitle(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		r=""
		while n>0:
			z=n%26
			if z==0:
				z=26
				n-=1
			r+=chr(z+64)
			n/=26
		return r[::-1]