#Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
#
#Example 1:
#Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
#Return 16
#The two words can be "abcw", "xtfn".
#
#Example 2:
#Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
#Return 4
#The two words can be "ab", "cd".
#
#Example 3:
#Given ["a", "aa", "aaa", "aaaa"]
#Return 0
#No such pair of words.

class Solution(object):
	def maxProduct(self, words):
		"""
		:type words: List[str]
		:rtype: int
		"""
		l=[]
		mx=0
		for i in words:
			t=[0 for _ in xrange(26)]
			for j in i:
				t[ord(j)-ord('a')]=1
			x=0
			for j in t:
				x=x*2 + j
			l.append(x)
		for i in xrange(len(words)):
			for j in xrange(i+1,len(words)):
				if not l[i]&l[j]:
					mx=max(mx,len(words[i])*len(words[j]))
		return mx