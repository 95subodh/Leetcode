#Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
class Solution(object):
    def isPowerOfFour(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		return (num > 0) and ((num & (num - 1)) == 0) and ((num & 0x5555555555555555l) == num)