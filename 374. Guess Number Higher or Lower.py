#We are playing the Guess Game. The game is as follows:
#
#I pick a number from 1 to n. You have to guess which number I picked.
#
#Every time you guess wrong, I'll tell you whether the number is higher or lower.
#
#You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
	def guessNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		high=n
		low=1
		chk=(high+low)/2
		res=guess(chk)
		while res!=0:
			if res==1:
				low=chk+1
			elif res==-1:
				high=chk-1
			else:
				break
			chk=(low+high)/2
			res=guess(chk)
		return chk