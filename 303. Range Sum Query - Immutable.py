Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

class NumArray(object):
	def __init__(self, nums):
		"""
		initialize your data structure here.
		:type nums: List[int]
		"""
		self.pre=[0]
		for i in xrange(len(nums)):
			self.pre.append(self.pre[-1]+nums[i])

	def sumRange(self, i, j):
		"""
		sum of elements nums[i..j], inclusive.
		:type i: int
		:type j: int
		:rtype: int
		"""
		return self.pre[j+1]-self.pre[i]
		

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)