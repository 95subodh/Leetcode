#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
class Solution(object):
	def merge(self, A, m, B, n):
		"""
		:type A: List[int]
		:type m: int
		:type B: List[int]
		:type n: int
		:rtype: void Do not return anything, modify nums1 in-place instead.
		"""
		indA = m-1;
		indB = n-1;
		while indA >=0 and indB>=0:
			if A[indA] > B[indB]:
				A[indA+indB+1] = A[indA]
				indA -= 1
			else:
				A[indA+indB+1] = B[indB]
				indB -= 1
		while indB >= 0:
			 A[indB] = B[indB]
			 indB -= 1