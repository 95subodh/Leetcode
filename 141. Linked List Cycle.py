#Given a linked list, determine if it has a cycle in it.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		turt=head
		hare=head
		while hare and hare.next:
			hare=hare.next.next
			turt=turt.next
			if hare==turt:
				return True
		return False