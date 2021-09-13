'''


Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0

 

Constraints:

    1 <= text.length <= 104
    text consists of lower case English letters only.




'''


from collections import Counter


class Solution:

	def maxNumberofBalloons( self, text : str ) -> int:

		instaces = Counter(text)

		print(instaces)

		count = 0

		while instaces['b'] > 0 and instaces['a'] > 0 and instaces['l'] > 1 and instaces['o'] > 1 and instaces['n'] > 0:

			count += 1 

			instaces['b'] -= 1
			instaces['a'] -= 1
			instaces['n'] -= 1
			instaces['l'] -= 2 
			instaces['o'] -= 2


		return count
