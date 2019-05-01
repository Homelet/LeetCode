class Solution:
	def convert(self, s: str, num_rows: int) -> str:
		period = num_rows * 2 - 2 if num_rows >= 2 else num_rows
		cycle = [s[index: index + period] for index in range(0, len(s), period)]
		buffer = []
		for line in range(num_rows):
			for c in cycle:
				if line == 0 or line == num_rows - 1:
					if line < len(c):
						buffer += c[line]
				else:
					first_index, second_index = line, period - line
					if first_index < len(c):
						buffer += c[first_index]
					if second_index < len(c):
						buffer += c[second_index]
		return "".join(buffer)


s1 = "PAYPALISHIRING"
print(Solution().convert(s1, 2))
