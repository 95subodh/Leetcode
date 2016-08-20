# Given an index k, return the kth row of the Pascal's triangle.
class Solution(object):
	def getRow(self, rowIndex):
		"""
        :type rowIndex: int
        :rtype: List[int]
		"""
		l=[]
		for i in xrange(rowIndex+1):
			z=[]
			for j in xrange(i+1):
				if j==0 or j==i:
					z.append(1)
				else:
					z.append(l[-1][j]+l[-1][j-1])
			l.append(z)
		return l[-1]