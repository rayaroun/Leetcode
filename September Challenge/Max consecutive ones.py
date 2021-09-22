# this was a simple challenge to find the maximum number of consecutive 1's appearing in a list


class Solution:
	def findMaxConsecutiveOnes(self, nums: List[int]) -> int:


		count = 0 

		tc = 0

		for num in nums:

			if num == 1:
				tc +=1
				count = max(count, tc)
				
			else:
				tc = 0
				
		return count
