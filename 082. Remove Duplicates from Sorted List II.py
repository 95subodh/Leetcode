# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		temp=head
		while temp:
			z=temp.val
			if temp==head and temp.next and temp.next.val==z:
				temp2=temp.next
				while temp2 and temp2.val==z:
					temp2=temp2.next
				head=temp=temp2
			elif temp.next and temp.next.next and temp.next.val==temp.next.next.val:
				temp2=temp.next
				z2=temp2.val
				while temp2 and temp2.val==z2:
					temp2=temp2.next
				temp.next=temp2
			else:
				temp=temp.next
					
		return head
