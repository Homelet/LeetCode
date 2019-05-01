class Solution:
	def isPalindrome(self, x: int) -> bool:
		x = str(x)
		left_index, right_index = 0, len(x) - 1
		while left_index < right_index:
			if x[left_index] != x[right_index]:
				return False
			left_index += 1
			right_index -= 1
		return True


i1 = 121

print(Solution().isPalindrome(i1))
