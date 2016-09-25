#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
#How many possible unique paths are there?
class Solution(object):
    def uniquePaths(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		l=[[0 for i in xrange(n)] for i in xrange(m)]
		for i in xrange(m):
			for j in xrange(n):
				if i==0 or j==0:
					l[i][j]=1
				else:
					l[i][j]+=l[i-1][j]+l[i][j-1]
		return l[m-1][n-1]