class Solution:
	def shiftingLetters(self, s: str, shifts: List[int]) -> str:

		final_list = []

		sumlist = sum(shifts)

		for i,num in enumerate(shifts):
			start = ord( s[i] ) - 97
			offset = (( start + sumlist ) % 26 ) + 97
			final_list.append(chr(offset))

			sumlist -= num
     
    return "".join(final_list)
