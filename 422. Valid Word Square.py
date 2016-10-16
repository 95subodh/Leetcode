#Given a sequence of words, check whether it forms a valid word square.
#
#A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
#
#Note:
#The number of words given is at least 1 and does not exceed 500.
#Word length will be at least 1 and does not exceed 500.
#Each word contains only lowercase English alphabet a-z.

class Solution(object):
	def validWordSquare(self, words):
		"""
		:type words: List[str]
		:rtype: bool
		"""
		for i in xrange(len(words)):
			for j in xrange(len(words[i])):
				if not j<len(words) or not i<len(words[j]) or words[i][j]!=words[j][i]:
					return False
		return True