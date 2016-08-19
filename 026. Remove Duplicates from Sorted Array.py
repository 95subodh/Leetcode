#Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#Do not allocate extra space for another array, you must do this in place with constant memory.
class Solution(object):
    def removeDuplicates(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	j=1
	if len(nums)<1:return 0
	for i in xrange(1,len(nums)):
		if nums[i]!=nums[i-1]:
			nums[j]=nums[i]
			j+=1
	return j