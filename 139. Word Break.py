#Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: Set[str]
		:rtype: bool
		"""
		l=[0 for i in xrange(len(s)+1)]
		for i in xrange(len(s)):
			for j in xrange(i,len(s)+1):
				if s[i:j] in wordDict and (l[i-1] or i==0):
					l[j-1]=1
		return True if l[len(s)-1] else False