'''

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26

 

Constraints:

    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] contains only lower case English letters.


'''


from typing import List
import itertools

class Solution:
	def maxLength(self, arr: List[str]) -> int:
		

		maxlength = 0

		for i in range(0,len(arr)+1):
			tl = list(itertools.combinations(arr,i))
			tl = [ "".join(e) for e in tl ]
			
			for element in tl:
				if len(set(element)) == len(element):
					if len(element)>maxlength:
						maxlength = len(element)

		return maxlength		
