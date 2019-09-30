from typing import List


class Solution:
	def trap(self, height: List[int]) -> int:
		result = [self.cal(height, i) for i in range(len(height) - 1)]
		print(result)
		return sum(result)
	
	
	def cal(self, height, index):
		if height[index] == 0:
			return 0
		result = [self.find_length(height, depth + 1, index) for depth in range(height[index])]
		print(result)
		return sum(result)
	
	
	def find_length(self, height, target_value, index):
		index_2 = index + 1
		while index_2 < len(height) and height[index_2] < target_value:
			if index_2 + 1 == len(height):
				return 0
			index_2 += 1
		return index_2 - index - 1


class Solution2:
	def trap(self, height: List[int]) -> int:
		"""
		determine the layer one by one and tests any point that could hold water
		:param height:
		:return:
		"""
		if len(height) == 0:
			return 0
		max_height = max(height)
		maps = [[0 if height[index] + layer < max_height else 1 for index in range(len(height))] for layer in range(max_height)]
		water = 0
		for layer in range(max_height - 1, -1, -1):
			# in order to contain water, the block has to be empty and have a left, a right
			water += self.check_layer(maps, layer, height)
		for l in maps:
			print(l)
		return water
	
	
	def check_layer(self, maps, layer, height):
		index = 0
		can_contain = False
		buffer = 0
		water = 0
		while index < len(height):
			if maps[layer][index] is 1:
				if can_contain:
					water += buffer
					buffer = 0
				else:
					can_contain = True
			else:
				if can_contain:
					buffer += 1
			index += 1
		return water


class Solution3:
	def trap(self, height: List[int]) -> int:
		if len(height):
			return 0
		ans = 0
		size = len(height)
		left_max, right_max = [0] * size, [0] * size
		left_max[0] = height[0]
		for index in range(1, size):
			left_max[index] = max(height[index], left_max[index - 1])
		right_max[size - 1] = height[size - 1]
		for index in range(size - 2, -1, -1):
			right_max[index] = max(height[index], right_max[index + 1])
		for index in range(1, size):
			ans += min(left_max[index], right_max[index]) - height[index]
		return ans
	
	
	t1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
	t2 = [2, 0, 2]
	print(Solution2().trap(t2))
