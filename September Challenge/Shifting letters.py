'''

You are given a string s of lowercase English letters 
and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, 
(wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.

 

Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.

Example 2:

Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"



unicode for a = 97 z = 122




'''



#this method is quite inefficient


class Solution:
	def shiftingLetters(self, s: str, shifts: List[int]) -> str:

    start_character = 97

      for i,number in enumerate(shifts):


        start = ord (s[i]) - start_character
        offset = (( start + shifts[i] ) % 26 ) + start_character 
        tc = chr(offset)


        if final_list:
          for j,element in enumerate(final_list):

            sto = ord(element) - start_character
            off = (( sto + shifts[i] ) % 26 ) + start_character 

            final_list[j] = chr(off)


        final_list.append(tc)

      return "".join(final_list))
