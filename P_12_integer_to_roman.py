class Solution:
	def __init__(self):
		self.maps = [
			[1000, "M"],
			[500, "D"],
			[100, "C"],
			[50, "L"],
			[10, "X"],
			[5, "V"],
			[1, "I"],
		]
	
	
	def intToRoman(self, num: int):
		s = []
		size = len(self.maps)
		while num != 0:
			for index in range(size):
				value, sym = self.maps[index]
				if num >= value:
					num -= value
					s.append(sym)
					break
				elif index + 1 < size:
					# find the fill number
					fill_value, fill_sym = self.maps[index + (2 - index % 2)]
					if num + fill_value >= value:
						num += fill_value - value
						s.append(fill_sym)
						s.append(sym)
						break
		return "".join(s)


t1 = 1994

print(Solution().intToRoman(t1))
