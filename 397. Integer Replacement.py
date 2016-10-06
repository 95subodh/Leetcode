#Given a positive integer n and you can do operations as follow:
#
#If n is even, replace n with n/2.
#If n is odd, you can replace n with either n + 1 or n - 1.
#What is the minimum number of replacements needed for n to become 1?

class Solution(object):
	def integerReplacement(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		cnt=0
		while n!=1:
			if n < 4:
				cnt+= [0, 0, 1, 2][n] - 1
				n=1
			elif n%4==1:n-=1
			elif n%4==3:n+=1
			else:n/=2
			cnt+=1
		return cnt