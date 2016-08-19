#Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
class Solution(object):
    def countBits(self, num):
	"""
	:type num: int
	:rtype: List[int]
	"""
	l=[0,1,1,2]
	for i in xrange(4,num+1):
		l.append((i&1)+l[i/2])
	return l[:num+1]