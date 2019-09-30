from typing import List
import itertools


class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		return [list(i) for i in list(set([tuple(sorted([n1, n2, n3, n4])) for n1, n2, n3, n4 in itertools.combinations(nums, 4) if n1 + n2 + n3 + n4 == target]))]


t1 = [1, 0, -1, 0, -2, 2]
t2 = [-497, -480, -477, -470, -452, -448, -440, -412, -390, -381, -372, -372, -369, -366, -355, -346, -340, -337, -322, -321, -311, -296, -258, -249, -248, -232, -215, -199, -174, -154, -128, -122, -122, -117, -115, -113, -110, -89, -86, -84, -78, -71, -69, -53, -49, -35, -25, -21, -7, 3, 7, 21, 25, 30, 47, 52, 81, 84, 87, 91, 96, 157, 161, 167, 178, 184, 210, 217, 228, 236, 274, 277, 283, 286, 290, 301, 302, 341, 352, 354, 361, 367, 384, 390, 412, 421, 458, 468, 483, 484, 486, 487, 490, 491]

t1_target = 0
t2_target = 8377

print(Solution().fourSum(t2, t2_target))
