#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#Example 1:
#
#11110
#11010
#11000
#00000
#Answer: 1
#
#Example 2:
#
#11000
#11000
#00100
#00011
#Answer: 3
#
#Credits:
#Special thanks to @mithmatt for adding this problem and creating all test cases.

class Solution(object):
	def numIslands(self, grid2):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		c=-1
		grid=[]
		for i in xrange(len(grid2)):
			grid.append(map(int, list(grid2[i])))
		for i in xrange(len(grid)):
			for j in xrange(len(grid[0])):
				if grid[i][j]==1:
					q=[[i,j]]
					while q:
						z=q.pop()
						grid[z[0]][z[1]]=c
						if z[0]+1<len(grid) and grid[z[0]+1][z[1]]==1:
							q.append([z[0]+1,z[1]])
						if z[0]-1>=0 and grid[z[0]-1][z[1]]==1:
							q.append([z[0]-1,z[1]])
						if z[1]+1<len(grid[0]) and grid[z[0]][z[1]+1]==1:
							q.append([z[0],z[1]+1])
						if z[1]-1>=0 and grid[z[0]][z[1]-1]==1:
							q.append([z[0],z[1]-1])
					c-=1
		return c*-1-1