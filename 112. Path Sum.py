#Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
#
#For example:
#Given the below binary tree and sum = 22,
#						5
#					   / \
#					  4   8
#					 /    / \
#					11   13  4
#				  /   \       \
#				 7    2        1
#return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		def sol( root, val, sum):
			if not root.left and not root.right and sum==val+root.val:
				return True
			a=b=False
			if root.left:
				a = sol(root.left, val+root.val, sum)
			if root.right:
				b = sol(root.right, val+root.val, sum)
			return a or b
		return sol(root, 0, sum) if root else False