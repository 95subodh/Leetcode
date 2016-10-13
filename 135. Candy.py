#There are N children standing in a line. Each child is assigned a rating value.
#
#You are giving candies to these children subjected to the following requirements:
#
#Each child must have at least one candy.
#Children with a higher rating get more candies than their neighbors.
#What is the minimum candies you must give?

class Solution(object):
	def candy(self, ratings):
		"""
		:type ratings: List[int]
		:rtype: int
		"""
		candies=[0 for i in xrange(len(ratings))]
		candies[0]=1
		for i in xrange(1,len(ratings)):
			if ratings[i]>ratings[i-1]:
				candies[i]=candies[i-1]+1
			else:
				candies[i]=1
		for i in xrange(len(ratings)-2,-1,-1):
			if ratings[i]>ratings[i+1]:
				candies[i]=max(candies[i+1]+1,candies[i])
		return sum(candies)