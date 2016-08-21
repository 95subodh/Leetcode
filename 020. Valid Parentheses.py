#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		l=[]
		for i in s:
			if i in '[({':
				l.append(i)
			elif len(l) and ord(i)<ord(l[-1])+3:
				l.pop()
			else:
				return False			
		return not len(l)