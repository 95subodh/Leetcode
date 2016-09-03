#Given a roman numeral, convert it to an integer.
#
#Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
		ans=romans[s[0]]
		for i in xrange(1,len(s)):
			if romans[s[i]]>romans[s[i-1]]:
				ans+=romans[s[i]]-2*romans[s[i-1]]
			else:
				ans+=romans[s[i]]
		return ans