# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		def sol(srt,end):
			if srt==end:
				return None
			mid=srt+(end-srt)/2
			root=TreeNode(nums[mid])
			root.left = sol(srt, mid)
			root.right = sol(mid+1, end)
			return root
		return sol(0, len(nums))
