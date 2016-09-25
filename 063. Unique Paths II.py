#Follow up for "Unique Paths":
#
#Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
#An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
#For example,
#There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
#[
#	[0,0,0],
#	[0,1,0],
#	[0,0,0]
#]
#The total number of unique paths is 2.
#
#Note: m and n will be at most 100.
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
		"""
		:type obstacleGrid: List[List[int]]
		:rtype: int
		"""
		m,n=len(obstacleGrid),len(obstacleGrid[0])
		l=[[0 for i in xrange(n)] for i in xrange(m)]
		for i in xrange(m):
			for j in xrange(n):
				if obstacleGrid[i][j]==0:
					if i==0 and j==0:
						l[i][j]=1
					elif i==0:
						l[i][j]=l[i][j-1]
					elif j==0:
						l[i][j]=l[i-1][j]
					else:
						l[i][j]+=l[i-1][j]+l[i][j-1]
		return l[m-1][n-1]
