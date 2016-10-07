#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#For example, 
#Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		mx=lt=rt=0
		left_trap, right_trap=[], []
		
		for i in xrange(len(height)):
			left_trap.append(lt)
			if height[i]>lt:
				lt=height[i]
				
		for i in xrange(len(height)-1,-1,-1):
			right_trap.append(rt)
			if height[i]>rt:
				rt=height[i]
				
		right_trap=right_trap[::-1]
		
		for i in xrange(len(height)):
			mx+=max(0,min(left_trap[i],right_trap[i])-height[i])
		return mx