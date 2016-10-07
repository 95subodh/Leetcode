#Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
#Note: You may not slant the container.

class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		mx,i,j=0,0,len(height)-1
		while i<j:
			mx=max(mx,min(height[i],height[j])*(j-i))
			if height[i]<height[j]:
				i+=1
			else:
				j-=1
		return mx