#Given two binary strings, return their sum (also a binary string).
class Solution(object):
    def addBinary(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		return bin(int(a,2)+int(b,2))[2:]