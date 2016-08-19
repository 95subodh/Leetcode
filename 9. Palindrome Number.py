#Determine whether an integer is a palindrome. Do this without extra space.
class Solution(object):
	    def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		z=str(x)[::-1]
		return True if z==str(x) else False