#Given a singly linked list, determine if it is a palindrome.
#
#Follow up:
#Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		hare = head
		rev = None
		while hare and hare.next:
			hare = hare.next.next
			temp = head.next
			head.next = rev
			rev = head
			head = temp
		
		tail = head.next if hare else head
		
		while tail:
			if rev.val != tail.val:
				return False
			rev=rev.next
			tail=tail.next
		
		return True		