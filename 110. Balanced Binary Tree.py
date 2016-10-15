#Given a binary tree, determine if it is height-balanced.
#
#For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if root is None:
			return True
		
		def check(l):
			if l[0] is None and l[1] is None:
				return [True, l[2], l[2]]
				
			elif l[0] is None:
				x=check([l[1].left, l[1].right, l[2]+1])
				return [max(x[1],x[2])<=l[2]+1 and x[0], l[2], max(x[1],x[2])]
				
			elif l[1] is None:
				x=check([l[0].left, l[0].right, l[2]+1])
				return [max(x[1],x[2])<=l[2]+1 and x[0], max(x[1],x[2]), l[2]]
				
			x=check([l[0].left, l[0].right, l[2]+1])
			y=check([l[1].left, l[1].right, l[2]+1])
			return [x[0] and y[0] and abs( max(x[1],x[2]) - max(y[1],y[2]) ) < 2, max(x[1],x[2]), max(y[1],y[2])]
		
		return check([root.left, root.right, 1])[0]