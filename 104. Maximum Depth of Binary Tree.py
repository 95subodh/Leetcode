#Given a binary tree, find its maximum depth.
#
#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		a=b=0
		if not root:
		    return 0
		if root.left is not None:
			a=self.maxDepth(root.left)
		if root.right is not None:
			b=self.maxDepth(root.right)
		return 1+max(a,b)