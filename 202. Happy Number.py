#Write an algorithm to determine if a number is "happy".
#
#A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

class Solution(object):
    def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		dict={}
		while 1:
			n=sum([int(i)**2 for i in str(n)])
			if n==1:
				return True
			elif n in dict:
				return False
			dict[n]=1