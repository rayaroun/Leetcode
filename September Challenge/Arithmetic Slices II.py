'''

Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

    For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
    For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.

A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

    For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].

The test cases are generated so that the answer fits in 32-bit integer.

 

Example 1:

Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

Example 2:

Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.

 

Constraints:

    1  <= nums.length <= 1000
    -231 <= nums[i] <= 231 - 1




'''


# The method is inefficient for sure. Need to find out how to make it better


from typing import List
import itertools

from itertools import combinations

class Solution:
	def numberOfArithmeticSlices(self, nums: List[int]) -> int:
		


		if all([nums[0] == x for x in nums]):

			total = 0	
			for r in range(3, len(nums) + 1):
				out = []
			
				for c in combinations(nums, r):
					out.append(c)
				
				total = total + len(out)

			return total
				


		else:

			def checkFunctions(a):
				if (any ((a[0] - a[1]) != a[x] - a[x+1] for x in range(1,len(a)-1) )):
					return 0
				else: 
					return 1 


			total = 0

			
			for r in range(3, len(nums) + 1):
				out = []
				
				for c in combinations(nums, r):
					out.append(c)
				
				# print(out)
			


				for element in out:
					if(checkFunctions(element) == 1):
						print(element) 
						total = total + 1
			

			
			return total



Solution.numberOfArithmeticSlices(Solution, [2,2,3,4])




