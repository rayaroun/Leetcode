'''


Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

 

Constraints:

    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.


'''



import numpy as np

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        elif s == t:
            return s

        i = len(t)


        final_min = len(s)

        while i < len(s):
            if list(np.intersect1d(list(t), list(s[:i]))) == list(t):
                

                revcounter_real = 0
                startpoint_real = 0

                while revcounter_real < i-len(t):
                  

                    if list(np.intersect1d(list(t), list(s[startpoint_real:i]))) == list(t):
                        startpoint_real += 1
                        continue

                    else:

                        return s[startpoint_real-1:i]
                        break

                    
                    revcounter += 1
        
                break
            
            
            
            
            i+=1

                




