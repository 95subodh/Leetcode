#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#For example, given n = 3, a solution set is:
#
#[
#	"((()))",
#	"(()())",
#	"(())()",
#	"()(())",
#	"()()()"
#]

class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		l=[]
		def gen(s,r,n):
			if n==0:
				l.append(s)
			else: 
				if n>r:gen(s+"(",r+1,n-1)
				if r>0:gen(s+")",r-1,n-1)
		gen("",0,n*2)
		return l
