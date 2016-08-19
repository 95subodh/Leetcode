#Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
class Solution(object):
    def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		profit=0
		if len(prices):
		    buy=prices[0]
		for i in xrange(1,len(prices)):
			if prices[i]<prices[i-1]:
				profit+=prices[i-1]-buy
				buy=prices[i]
		if len(prices):
		    profit+=prices[-1]-buy
		return profit