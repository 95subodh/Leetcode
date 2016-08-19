#Given two strings s and t, write a function to determine if t is an anagram of s.
class Solution(object):
    def isAnagram(self, s, t):
	"""
	:type s: str
	:type t: str
	:rtype: bool
	"""
	return True if sorted(s)==sorted(t) else False