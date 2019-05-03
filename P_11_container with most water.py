import itertools
from typing import List


class Solution:
	def maxArea(self, height: List[int]) -> int:
		maxArea = 0
		for index_1, index_2 in itertools.combinations(range(len(height)), 2):
			maxArea = max((index_2 - index_1) * min(height[index_1], height[index_2]), maxArea)
		return maxArea


t1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(Solution().maxArea(t1))
