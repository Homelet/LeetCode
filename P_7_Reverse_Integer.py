class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		x = str(x)
		# test is the int negative
		negative = x.startswith('-')
		
		# reverse the int
		int_string = "".join(x.replace("-", "")[::-1])
		
		# create the integer this also remove all leading 0
		integer = int("-" + int_string) if negative else int(int_string)
		if -(2 ** 31) <= integer <= 2 ** 31 - 1:
			return integer
		return 0


i = 1534236469

print(Solution().reverse(i))
