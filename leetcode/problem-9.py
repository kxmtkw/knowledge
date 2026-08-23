# -------------------------
# Palindrome Number
# -------------------------


# -------------------------
#
# First Approach
#
# Convert the number into a string and check whether that string is a palindrome by iterating over length/2 items.
# - O(n) time
#
# -------------------------


class Solution(object):

	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""

		string = str(x)

		length = len(string)

		for i in range(length//2):
			if string[i] != string[length-i-1]:
				return False

		return True

		
		