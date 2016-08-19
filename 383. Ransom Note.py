#Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
		"""
		:type ransomNote: str
		:type magazine: str
		:rtype: bool
		"""
		l=[0 for i in xrange(26)]
		for i in magazine:
			l[ord(i)-97]+=1
		for i in ransomNote:
			if l[ord(i)-97]>0:
				l[ord(i)-97]-=1
			else:
				return False
		return True