#Given an input string, reverse the string word by word.
#
#For example,
#Given s = "the sky is blue",
#return "blue is sky the".
#
#Update (2015-02-12):
#For C programmers: Try to solve it in-place in O(1) space.

class Solution(object):
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		l=list(s.split(' '))
		l=filter(None, l)
		l= l[::-1]
		z=""
		for i in xrange(len(l)):
			if i>0:
				z+=" "
			z+=l[i]
		return z