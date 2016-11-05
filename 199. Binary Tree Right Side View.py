#Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
#For example:
#Given the following binary tree,
#	1            <---
# /   \
#2     3         <---
# \     \
#  5     4       <---
#You should return [1, 3, 4].
#
#Credits:
#Special thanks to @amrsaqr for adding this problem and creating all test cases.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		q=[]
		visited=[]
		if root:
			q.append(root)
		while q:
			qnew=[]
			visited.append(q[-1].val)
			for i in q:
				if i.left:
					qnew.append(i.left)
				if i.right:
					qnew.append(i.right)
			q=qnew
		return visited