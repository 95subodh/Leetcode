#Given a string, find the length of the longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		dict={}
		mx=0
		prev=-1
		for i in xrange(len(s)):
			if s[i] in dict and dict[s[i]]>prev:
				prev=dict[s[i]]
			dict[s[i]]=i
			mx=max(mx,i-prev)
		return mx