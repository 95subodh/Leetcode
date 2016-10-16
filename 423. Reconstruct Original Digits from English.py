#Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.
#
#Note:
#Input contains only lowercase English letters.
#Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
#Input length is less than 50,000.
#Example 1:
#Input: "owoztneoer"
#
#Output: "012"
#Example 2:
#Input: "fviefuro"
#
#Output: "45"

class Solution(object):
	def originalDigits(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		l=[0 for i in xrange(26)]
		for i in s:
			l[ord(i)-ord('a')]+=1
		z=['zero','one','two','three','four','five','six','seven','eight','nine']
		ans=""
		xx=[0,8,6,2,4,7,5,1,9,3]
		k=0
		while k<10:
			i=xx[k]
			x=len(s)
			for j in z[i]:
				x=min(x,l[ord(j)-ord('a')])
			for j in xrange(x):
				ans+=str(i)
			for j in z[i]:
				l[ord(j)-ord('a')]-=x
			k+=1
		return "".join(sorted(ans))