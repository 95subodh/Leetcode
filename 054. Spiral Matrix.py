#Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
#For example,
#Given the following matrix:
#
#[
# [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
#]
#You should return [1,2,3,6,9,8,7,4,5].

class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if not matrix:return []
		ul,ur,dr,dl=1,len(matrix[0])-1,len(matrix)-1,0
		l=[]
		i,j=0,0
		while len(l)<len(matrix)*len(matrix[0])-1:
			while j<ur:
				l.append(matrix[i][j])
				j+=1
			while i<dr:
				l.append(matrix[i][j])
				i+=1
			while j>dl and len(l)<len(matrix)*len(matrix[0])-1:
				l.append(matrix[i][j])
				j-=1
			while i>ul and len(l)<len(matrix)*len(matrix[0])-1:
				l.append(matrix[i][j])
				i-=1
			ul+=1
			ur-=1
			dr-=1
			dl+=1
		return l+[matrix[i][j]] if len(l)<len(matrix)*len(matrix[0]) else l