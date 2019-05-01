class Solution:
	def myAtoi(self, s: str) -> int:
		flag = False
		has_digit = False
		buffer = []
		for index in range(len(s)):
			char = s[index]
			if char.isspace():
				if flag:
					break
				continue
			else:
				if not flag:
					if char.isdigit():
						flag = True
						buffer += char
						has_digit = True
					elif char == "+" or char == "-":
						flag = True
						buffer += char
					else:
						return 0
				else:
					if char.isdigit():
						buffer += char
						has_digit = True
					else:
						break
		result = "".join(buffer)
		if not has_digit or len(result) == 0:
			return 0
		integer = int(result)
		if -(2 ** 31) > integer:
			return -(2 ** 31)
		elif integer > 2 ** 31 - 1:
			return 2 ** 31 - 1
		else:
			return integer


t1 = "     -42"
t2 = "4193 with words"
t3 = "words and 987"
t4 = "-91283472332"
t5 = "   +0 123"

print(Solution().myAtoi(t5))
