#You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		i=c=0
		l3=ListNode(0)
		current=l3
		while l1 or l2:
			t=c
			if l1:
				t+=l1.val
				l1=l1.next
			if l2:
				t+=l2.val
				l2=l2.next
			print t
			current.next=ListNode(t%10)
			current=current.next
			c=t/10
		if c>0:
			current.next=ListNode(c)
		return l3.next