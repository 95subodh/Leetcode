#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
class Solution(object):
    def convert(self, s, numRows):
	"""
	:type s: str
	:type numRows: int
	:rtype: str
	"""
	l=["" for i in xrange(numRows)]
	i=0
	z=1
	for j in s:
		l[i]+=j
		if numRows==1:
			z=0
		elif i==numRows-1:
			z=-1
		elif i==0:
			z=1
		i+=z
	return "".join(l)
