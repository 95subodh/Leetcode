#Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#
#Follow up:
#Did you use extra space?
#A straight forward solution using O(mn) space is probably a bad idea.
#A simple improvement uses O(m + n) space, but still not the best solution.
#Could you devise a constant space solution?

class Solution(object):
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		for i in xrange(len(matrix)):
			f=0
			for j in xrange(len(matrix[0])):
				if matrix[i][j]==0: f=1
			for j in xrange(len(matrix[0])):
				if f and matrix[i][j]!=0: matrix[i][j]='x'

		k=len(matrix[0])
		for i in xrange(k):
			f=0
			for j in xrange(len(matrix)):
				if matrix[j][i]==0: f=1
			for j in xrange(len(matrix)):
				if f: matrix[j][i]='x'
		
		for i in xrange(len(matrix)):
			for j in xrange(k):
				if matrix[i][j]=='x':
					matrix[i][j]=0