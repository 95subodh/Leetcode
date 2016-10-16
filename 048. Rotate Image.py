#You are given an n x n 2D matrix representing an image.
#
#Rotate the image by 90 degrees (clockwise).
#
#Follow up:
#Could you do this in-place?

class Solution(object):
    def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		ln = len(matrix)
		x=ln/2+1 if ln&1 else ln/2
		for i in xrange(x):
			for j in xrange(i,ln-1-i):
				a=matrix[i][j]
				matrix[i][j]=matrix[ln-1-j][i]
				matrix[ln-1-j][i]=matrix[ln-1-i][ln-1-j]
				matrix[ln-1-i][ln-1-j]=matrix[j][ln-1-i]
				matrix[j][ln-1-i]=a