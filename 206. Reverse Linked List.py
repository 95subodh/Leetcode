#Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		back=head
		curr=None
		if back:
			curr=head.next
			back.next=None
		while curr:
			forw=curr.next
			curr.next=back
			back=curr
			curr=forw
		return back