#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
class Solution(object):
    def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		dict={}
		minInd=0
		for i in xrange(len(s)):
			if s[i] in dict:
				dict[s[i]]+=1
			else:
				dict[s[i]]=1
			while minInd<len(s) and s[minInd] in dict and dict[s[minInd]]>1:
				minInd+=1
			
		return -1 if minInd==len(s) else minInd