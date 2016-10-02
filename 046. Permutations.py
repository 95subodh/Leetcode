#Given a collection of distinct numbers, return all possible permutations.
#
#For example,
#[1,2,3] have the following permutations:
#[
#	[1,2,3],
#	[1,3,2],
#	[2,1,3],
#	[2,3,1],
#	[3,1,2],
#	[3,2,1]
#]

class Solution(object):
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		ans=[]
		used=[0 for i in xrange(len(nums))]
		def perm(curlist, used):
			if len(curlist)==len(nums):
				ans.append(curlist)
			else:
				for i in xrange(len(nums)):
					if not used[i]:
						used[i]=1
						perm(curlist+[nums[i]], used)
						used[i]=0
		perm([], used)
		return ans