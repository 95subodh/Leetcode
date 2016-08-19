#Given an integer, write a function to determine if it is a power of three.
from math import *
class Solution(object):
    def isPowerOfThree(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		return True if n>0 and 3**20%n==0 else False