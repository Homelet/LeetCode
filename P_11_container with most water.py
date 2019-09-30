import itertools
from typing import List


def maxArea_2(height: List[int]) -> int:
	maxArea = 0
	for index_1, index_2 in itertools.combinations(range(len(height)), 2):
		maxArea = max((index_2 - index_1) * min(height[index_1], height[index_2]), maxArea)
	return maxArea


class Solution:
	def maxArea(self, height: List[int]) -> int:
		left, right = 0, len(height) - 1
		maxArea = 0
		while left < right:
			maxArea = max((right - left) * min(height[left], height[right]), maxArea)
			if height[left] >= height[right]:
				flagValue = height[right]
				while left < right and height[right] <= flagValue:
					right -= 1
			else:
				flagValue = height[left]
				while left < right and height[left] <= flagValue:
					left += 1
		return maxArea


t1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(t1))
