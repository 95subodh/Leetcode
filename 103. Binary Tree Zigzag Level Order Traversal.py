#Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
#For example:
#Given binary tree [3,9,20,null,null,15,7],
#		3
#	   / \
#	  9  20
#		/  \
#	   15   7
#return its zigzag level order traversal as:
#[
#	[3],
#	[20,9],
#	[15,7]
#]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def zigzagLevelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		ans=[]
		child=[root]
		c=0
		while child:
			temp,temp2=[],[]
			for i in child:
				if i:
					temp.append(i.left)
					temp.append(i.right)
					temp2.append(i.val)
			if temp2:
				if c&1:
					ans.append(temp2[::-1])
				else:
					ans.append(temp2)
			c+=1
			child=temp
		return ans