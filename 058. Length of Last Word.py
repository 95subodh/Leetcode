#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
#If the last word does not exist, return 0.
class Solution(object):
    def lengthOfLastWord(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		s=map(str,s.split())
		return len(s[-1]) if len(s) else 0