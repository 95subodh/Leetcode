#Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
#You may assume no duplicates in the array.
#
#Here are few examples.
#[1,3,5,6], 5 → 2
#[1,3,5,6], 2 → 1
#[1,3,5,6], 7 → 4
#[1,3,5,6], 0 → 0

class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		low=0
		high=len(nums)-1
		if nums[high]<target:
			return high+1
		while low<high:
			mid=(low+high)/2
			if nums[mid]==target:
				return mid
			elif nums[mid]>target:
				high=mid
			else:
				low=mid+1
		return high