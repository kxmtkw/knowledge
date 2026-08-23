# -------------------------
# Add two numbers
# -------------------------


# -------------------------
#
# Final Approach
#
# Instead of treating them as linked lists. Just treat them as actual digits of a number and how you will add them. 
# It then becomes an iteration problem. Its a recursive approach.
# - O(n) time where n is the length of the longer list node
#
# -------------------------


# Definition for singly-linked list.
# class ListNode(object):
	
# 	def __init__(self, val=0, next=None):
# 		self.val = val
# 		self.next = next


class Solution(object):


	def add(self, head1, head2, carry):

		# if both heads are None, the digits have ended.
		if head1 is None and head2 is None:
			return ListNode(carry, None) if carry == 1 else None

		# equivalent to "padding" by zeros in case one number has already ended
		d1 = head1.val if head1 is not None else 0
		d2 = head2.val if head2 is not None else 0

		# summing up the digits and resolving the carry

		sum = d1 + d2 + carry
		carry = sum // 10
		sum = sum % 10

		# make the node for the current result and try to resolve the next pair of digits

		rhead = ListNode(sum, None)
		rhead.next = self.add(
			head1.next if head1 else None, 
			head2.next if head2 else None, 
			carry, 
		)

		return rhead
	
	
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: Optional[ListNode]
		:type l2: Optional[ListNode]
		:rtype: Optional[ListNode]
		"""
		return self.add(l1, l2, 0)
		
