#The count-and-say sequence is the sequence of integers beginning as follows:
#1, 11, 21, 1211, 111221, ...
#
#1 is read off as "one 1" or 11.
#11 is read off as "two 1s" or 21.
#21 is read off as "one 2, then one 1" or 1211.
#Given an integer n, generate the nth sequence.
class Solution(object):
    def countAndSay(self, A):
	"""
	:type n: int
	:rtype: str
	"""
	z=["0","1"]
	for i in xrange(1,A+1):
		s,n,c="",z[i][0],1
		for j in xrange(1,len(z[i])):
			if z[i][j]==n:c+=1
			else:
				s+=str(c)+n
				n=z[i][j]
				c=1
		s+=str(c)+n
		z.append(s)
	return z[A]