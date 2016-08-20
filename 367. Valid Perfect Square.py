#Given a positive integer num, write a function which returns True if num is a perfect square else False.
class Solution(object):
    def isPerfectSquare(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		return num==int(num**0.5)**2