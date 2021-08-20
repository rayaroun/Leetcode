"""


Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.


"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ls = list(s)
        lt = list(t)
        
        if len(t) != len(s):
            return False
        
        count = 0 
        
        sd = { item : 0 for item in ls }
        td = { item : 0 for item in lt }
        
        
        for item in ls:
            sd[item] = sd[item] + 1
            
        for item in lt:
            td[item] = td[item] + 1
            
        
        if sd == td:
            return True
        else:
            return False
            
            
                
        
