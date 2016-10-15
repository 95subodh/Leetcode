#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
#For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#	 1
#	/ \
#      2   2
#     / \ / \
#    3  4 4  3
#But the following [1,2,2,null,3,null,3] is not:
#	 1
#	/ \
#      2   2
#	\   \
#	3    3
#Note:
#Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if root is None:
			return True
		
		def check(l):
			for i in xrange(len(l)/2):
				if (l[i] or l[-(i+1)]) and (not l[i] or not l[-(i+1)] or l[i].val!=l[-(i+1)].val):
					return False
			z=[]
			for i in l:
				if i:
					z.append(i.left)
					z.append(i.right)
			return check(z) if len(z) else True
		
		return check( [root.left,root.right] )
