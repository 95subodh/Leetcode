#Given a non-negative number represented as an array of digits, plus one to the number.
#
#The digits are stored such that the most significant digit is at the head of the list.
class Solution(object):
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		c=1
		for i in xrange(len(digits)-1,-1,-1):
			if c+digits[i]==10:
				digits[i]=0
			elif c==1:
				digits[i]+=1
				c=0
		if c:
			digits=[1]+digits
		return digits