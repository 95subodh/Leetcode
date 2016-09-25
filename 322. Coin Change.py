#You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
#Example 1:
#coins = [1, 2, 5], amount = 11
#return 3 (11 = 5 + 5 + 1)
#
#Example 2:
#coins = [2], amount = 3
#return -1.
#
#Note:
#You may assume that you have an infinite number of each kind of coin.

class Solution(object):
	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		b=pow(10, 10)
		l=[b for i in xrange(amount+1)]
		l[0]=0
		for i in xrange(amount+1):
			for j in coins:
				if i>=j:
					l[i]=min(l[i],l[i-j]+1)
		return l[-1] if l[-1] < b else -1