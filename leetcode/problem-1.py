# -------------------------
# Two Sum
# -------------------------


# -------------------------
#
# First Approach
#
# Iterate over each element and look for any element in the array through a second loop to check whether it 
# adds up to target.
# - O(n^2) time
#
# Final Approach
#
# For each element x and target t, store (t - x: index) in a map. If t - x is encountered again in the array, 
# that means the required two numbers have been found. Then index of t - x can be obtained from the map and the index of x is just the 
# current loop index
# - O(n) time
#
# -------------------------


class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""

		delta_map = {}

		for i in range(len(nums)):

			if nums[i] in delta_map:
				return [delta_map[nums[i]], i]
			
			diff = target - nums[i]
			delta_map[diff] = i