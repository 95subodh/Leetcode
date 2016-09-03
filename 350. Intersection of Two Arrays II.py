#Given two arrays, write a function to compute their intersection.

class Solution(object):
    def intersect(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		dict = collections.defaultdict(int)
		for i in nums1:
			dict[i]+=1
		ans=[]
		for i in nums2:
			if dict[i]>0:
				ans.append(i)
				dict[i]-=1
		return ans