#Given a binary tree, return all root-to-leaf paths.
#
#For example, given the following binary tree:
#
#	1
#     /   \
#    2     3
#     \
#      5
#All root-to-leaf paths are:
#
#["1->2->5", "1->3"]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {string[]}
	def binaryTreePaths(self, root):
		ans=[]
		def findpath(root, path):
			if not root:
				return
			if not root.left and not root.right:
				ans.append((path+"->"+str(root.val))[2:])
				print ans
			if root.left:
				findpath(root.left, path+"->"+str(root.val))
			if root.right:
				findpath(root.right, path+"->"+str(root.val))
		findpath(root,"")
		return ans
