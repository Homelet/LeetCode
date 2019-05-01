class Solution:
	def numJewelsInStones(self, J: str, S: str) -> int:
		J = list(J)
		S = list(S)
		counter = 0
		for s in S:
			if s in J:
				counter += 1
		return counter
