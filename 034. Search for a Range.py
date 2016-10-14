#Given a sorted array of integers, find the starting and ending position of a given target value.
#
#Your algorithm's runtime complexity must be in the order of O(log n).
#
#If the target is not found in the array, return [-1, -1].
#
#For example,
#Given [5, 7, 7, 8, 8, 10] and target value 8,
#return [3, 4].

class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		lo=0
		hi=len(nums)-1
		while lo<hi:
			mid=(lo+hi)/2
			if nums[mid]>=target:
				hi=mid
			else:
				lo=mid+1
		if nums[lo]!=target:
			return [-1,-1]
		lower_index=lo
		lo=0
		hi=len(nums)-1
		while lo<hi:
			mid=(lo+hi)/2+1
			if nums[mid]<=target:
				lo=mid
			else:
				hi=mid-1
		return [lower_index,hi]