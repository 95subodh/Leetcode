#Write a program to find the n-th ugly number.
#
#Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
#
#Note that 1 is typically treated as an ugly number.

import heapq
class Solution(object):
	def nthUglyNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		l=[1]
		primes=[2,3,5]
		heapq.heapify(l)
		set1=set(l)
		n-=1
		while n>0:
			z=heapq.heappop(l)
			n-=1
			for i in primes:
				if z*i not in set1:
				    heapq.heappush(l, z*i)
				    set1.add(z*i)
		return heapq.heappop(l)