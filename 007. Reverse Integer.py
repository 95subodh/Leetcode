#Reverse digits of an integer.
class Solution(object):
    def reverse(self, x):
	"""
	:type x: int
	:rtype: int
	"""	
	f=1
	if x<0:
		f=-1
		x*=-1
	z=f*int(str(x)[::-1]) 
	if abs(z)>2147483641:return 0
	else:return z
