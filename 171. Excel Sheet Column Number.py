#Given a column title as appear in an Excel sheet, return its corresponding column number.
class Solution(object):
    def titleToNumber(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		s=s[::-1]
		ans=0
		for i in xrange(len(s)):
			ans+=pow(26, i)*(ord(s[i])-64)
		return ans