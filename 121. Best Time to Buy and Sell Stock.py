#Say you have an array for which the ith element is the price of a given stock on day i.
#
#If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
class Solution(object):
    def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		mprofit=0
		if len(prices):
			minele=prices[0]
		for i in prices:
			if i<minele:
				minele=i
			mprofit=max(mprofit,i-minele)
		return mprofit