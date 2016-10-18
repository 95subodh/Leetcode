#Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
#
#Note:
#n is positive and will fit within the range of a 32-bit signed integer (n < 231).
#
#Example 1:
#
#Input:
#3
#
#Output:
#3
#Example 2:
#
#Input:
#11
#
#Output:
#0
#
#Explanation:
#The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

import math
class Solution(object):
	def findNthDigit(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		x,k=9,1
		while n>x*k:
			n-=x*k
			k+=1
			x*=10
		return int(str(pow(10, k-1)-1+int(math.ceil(n*1.0/k)))[n%k-1])