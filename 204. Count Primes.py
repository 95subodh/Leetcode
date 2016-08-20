#Count the number of prime numbers less than a non-negative number, n.
class Solution(object):
	def primes(self, n):
		""" Returns  a list of primes < n """
		sieve = [True] * n
		for i in xrange(3,int(n**0.5)+1,2):
			if sieve[i]:
				sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
		return [2] + [i for i in xrange(3,n,2) if sieve[i]]
		
	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		return len(self.primes(n)) if n>2 else 0