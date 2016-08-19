#Write a program to check whether a given number is an ugly number.
#
#Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
class Solution(object):
    def isUgly(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num==0:return False
		while num%2==0:
			num/=2
		while num%3==0:
			num/=3
		while num%5==0:
			num/=5
		return True if num==1 else False