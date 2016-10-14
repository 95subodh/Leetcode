#Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.
#
#Note:
#
#The length of both num1 and num2 is < 5100.
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.
#You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
	def addStrings(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		l, i, c, num1, num2 = [], 0, 0, num1[::-1], num2[::-1]
		while i<len(num1) or i<len(num2):
			t1=t2=0
			if i<len(num1):
				t1=int(num1[i])
			if i<len(num2):
				t2=int(num2[i])
			t=t1+t2+c
			c=t/10
			l.append(str(t%10))
			i+=1
		if c>0:
			l.append(str(c))
		return "".join(l)[::-1]