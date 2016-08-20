#Write a function that takes a string as input and reverse only the vowels of a string.
class Solution(object):
    def reverseVowels(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		i=0
		j=len(s)-1
		s=list(s)
		vowel="aeiouAEIOU"
		while i<j:
			while i<j and s[i] not in vowel:
				i+=1
			while i<j and s[j] not in vowel:
				j-=1
			if s[i] in vowel and s[j] in vowel:
				t=s[i]
				s[i]=s[j]
				s[j]=t
			i+=1
			j-=1
		return "".join(s)

print Solution().reverseVowels("aO")