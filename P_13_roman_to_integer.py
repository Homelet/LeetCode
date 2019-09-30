class Solution:
	def __init__(self):
		self.maps = {
			"M": 1000,
			"D": 500,
			"C": 100,
			"L": 50,
			"X": 10,
			"V": 5,
			"I": 1,
		}
	
	
	def romanToInt(self, s: str) -> int:
		s = [self.maps[letter] for letter in s]
		value = 0
		index = 0
		while index < len(s):
			# if next one is bigger than this one, means this is a group
			if index + 1 < len(s) and s[index + 1] > s[index]:
				value += s[index + 1] - s[index]
				index += 2
			else:
				value += s[index]
				index += 1
		return value


t1 = "LVIII"

print(Solution().romanToInt(t1))
