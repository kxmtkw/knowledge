# -------------------------
# Median of Two Sorted Arrays
# -------------------------


# -------------------------
#
# First Approach
#
# Since the arrays are sorted, we can combine and sort them at once linearly to get a single merged array.
# Then finding the median is trivial.
# - O(n+m)
#
# -------------------------


import math


class Solution(object):
	
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""

		merged_array = []

		i1 = 0
		i2 = 0

		for i in range(len(nums1) + len(nums2)):

			if i1 >= len(nums1):
				merged_array.append(nums2[i2])
				i2 += 1
				continue
			elif i2 >= len(nums2):
				merged_array.append(nums1[i1])
				i1 += 1
				continue

			if nums1[i1] < nums2[i2]:
				merged_array.append(nums1[i1])
				i1 += 1
			elif nums1[i1] > nums2[i2]:
				merged_array.append(nums2[i2])
				i2 += 1
			else:
				merged_array.append(nums2[i2])
				i2 += 1

		median_index = float((len(merged_array) - 1)) / 2.0
		median_high = int(math.ceil(median_index))
		median_low = int(math.floor(median_index))

		median = (merged_array[median_high] + merged_array[median_low]) / 2.0

		return median