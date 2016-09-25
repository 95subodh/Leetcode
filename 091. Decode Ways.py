#A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
#'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
#Given an encoded message containing digits, determine the total number of ways to decode it.
#
#For example,
#Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
#The number of ways decoding "12" is 2.

class Solution(object):
    def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		l=[[0,0],[1,1]]
		for i in xrange(1,len(s)):
			if int(s[i])==0 and int(s[i-1])==0:
				return 0
			if int(s[i])==0 and int(s[i-1])*10+int(s[i])<27:
			    l.append( [ l[-1][1], 0 ] )
			elif int(s[i])==0:
				l.append([0,0])
			elif int(s[i-1])*10+int(s[i])<27:
				l.append( [ sum(l[-1]), l[-1][0] ] )
			else:
				l.append( [ l[-1][0], l[-1][0] ] )
		return l[-1][0] if len(s) and int(s[0]) else 0