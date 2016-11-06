#Given a binary tree, flatten it to a linked list in-place.
#
#For example,
#Given
#
#		   1
#		  / \
#		 2   5
#		/ \   \
#	   3   4   6
#The flattened tree should look like:
#	1
#	 \
#	  2
#		\
#		 3
#		  \
#			4
#			 \
#			  5
#				\
#				 6
#click to show hints.
#
#Hints:
#If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def flatten(self, root):
		"""
		:type root: TreeNode
		:rtype: void Do not return anything, modify root in-place instead.
		"""
		stk=[]
		visited=[]
		if root:
			stk=[root]
		while stk:
			z=stk.pop()
			visited.append(z.val)
			if z.right:
				stk.append(z.right)
			if z.left:
				stk.append(z.left)
				z.right=z.left
			elif z.right:
				z.right=z.right
			elif stk:
				z.right=stk[-1]
			z.left=None