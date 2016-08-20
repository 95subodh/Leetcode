#Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
class Solution(object):
    def addDigits(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		return 9 if num%9==0 and num>0 else num%9