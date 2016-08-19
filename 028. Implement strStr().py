#Implement strStr().
class Solution(object):
    def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		if len(needle)>len(haystack):return -1
		for i in xrange(len(haystack)-len(needle)+1):
			f=1
			for j in xrange(len(needle)):
				if haystack[i+j]!=needle[j]:
					f=0
					break
			if f==1:
				return i
		return -1