#Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
#This is case sensitive, for example "Aa" is not considered a palindrome here.
#
#Note:
#Assume the length of given string will not exceed 1,010.
#
#Example:
#
#Input:
#"abccccdd"
#
#Output:
#7
#
#Explanation:
#One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution(object):
    def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		dict={}
		mx=0
		for i in s:
			if i in dict:
				dict[i]+=1
			else:
				dict[i]=1
		for i in dict:
			mx+=dict[i]
			if dict[i]&1:
				mx-=1
		return mx+1 if mx<len(s) else mx