#Follow up for problem "Populating Next Right Pointers in Each Node".
#
#What if the given tree could be any binary tree? Would your previous solution still work?
#
#Note:
#
#You may only use constant extra space.
#For example,
#Given the following binary tree,
#			1
#		 /  \
#		2    3
#	  / \    \
#	 4   5    7
#After calling your function, the tree should look like:
#			1 -> NULL
#		 /  \
#		2 -> 3 -> NULL
#	  / \    \
#	 4-> 5 -> 7 -> NULL

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
				if z.right:
					z.left.next=z.right
				else:
					tmp=z.next
					while tmp:
						if tmp.left:
							tmp=tmp.left
							break
						if tmp.right:
							tmp=tmp.right
							break
						tmp=tmp.next
					z.left.next=tmp
				stk.append(z.left)
			
			if z.right:
				tmp=z.next
				while tmp:
					if tmp.left:
						tmp=tmp.left
						break
					if tmp.right:
						tmp=tmp.right
						break
					tmp=tmp.next
				z.right.next=tmp
				stk.append(z.right)