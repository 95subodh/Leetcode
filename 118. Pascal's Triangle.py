class Solution(object):
    def generate(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""
		l=[]
		for i in xrange(numRows):
			z=[]
			for j in xrange(i+1):
				if j==0 or j==i:
					z.append(1)
				else:
					z.append(l[-1][j]+l[-1][j-1])
			l.append(z)
		return l