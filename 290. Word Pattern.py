#Given a pattern and a string str, find if str follows the same pattern.
class Solution(object):
	def wordPattern(self, pattern, str):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""
		dict={}
		dict2={}
		str=list(str.split())
		if len(pattern)!=len(str):return False
		for i in xrange(len(pattern)):
			if pattern[i] in dict:
				if dict[pattern[i]]!=str[i] or dict2[str[i]]!=pattern[i]:
					return False
			else:
				if str[i] in dict2:
					return False
				dict[pattern[i]]=str[i]
				dict2[str[i]]=pattern[i]
		print dict,dict2
		return True