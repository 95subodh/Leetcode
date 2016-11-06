#Given a binary tree
#
#struct TreeLinkNode {
#	TreeLinkNode *left;
#	TreeLinkNode *right;
#	TreeLinkNode *next;
#}
#pulate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
#itially, all next pointers are set to NULL.
#
#te:
#
#u may only use constant extra space.
#u may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
#r example,
#ven the following perfect binary tree,
#	  1
#	 /  \
#	2    3
#      / \  / \
#     4  5  6  7
#ter calling your function, the tree should look like:
#	  1 -> NULL
#	 /  \
#	2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
	# @param root, a tree link node
	# @return nothing
	def connect(self, root):
		stk=[]
		if root:
			stk=[root]
			root=next = None
		while stk:
			z=stk.pop()
			if z.left:
				z.left.next=z.right
				stk.append(z.left)
			if z.right:
				if z.next:
					z.right.next=z.next.left
				else:
					z.right.next=None
				stk.append(z.right)
