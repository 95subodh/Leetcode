#Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def sortedListToBST(self, head):
		"""
		:type head: ListNode
		:rtype: TreeNode
		"""
		nums=[]
		while head:
			nums.append(head.val)
			head=head.next
		def sol(srt,end):
			if srt==end:
				return None
			mid=srt+(end-srt)/2
			root=TreeNode(nums[mid])
			root.left = sol(srt, mid)
			root.right = sol(mid+1, end)
			return root
		return sol(0, len(nums))