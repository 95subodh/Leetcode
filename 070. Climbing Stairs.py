#You are climbing a stair case. It takes n steps to reach to the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
class Solution(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		ways=[0,1,2]
		for i in xrange(n):
			ways.append(ways[-1]+ways[-2])
		return ways[n]