'''


Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

    For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

 

Example 1:

Input: strs = ["aba","cdc","eae"]
Output: 3

Example 2:

Input: strs = ["aaa","aaa","aa"]
Output: -1

 

Constraints:

    1 <= strs.length <= 50
    1 <= strs[i].length <= 10
    strs[i] consists of lowercase English letters.


'''



#This code is working for all the test cases. Was a very simple fix to get all the test cases working. All I had to include was a list which carries all the subsequence of elements that have been processed.

from typing import List
from itertools import combinations

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
        longelementlist = []
        iteration = 0
        
        def get_max_str(lst):
            return max(lst, key=len)

          
          
        #this if the function to get all the subsequences
        
        def get_all_substrings(input_string):
            out = set()
            for r in range(1, len(input_string) + 1):
                for c in combinations(input_string, r):
                    out.add(''.join(c))
            return sorted(out)

        

        def counterFunct(s):

            counter = 0
            longestElement = get_max_str(s)

            for element in s:

                if longestElement in element:
                    counter+=1
            return counter,longestElement

            

        def uslen(strs,iteration,longelementlist):
            
            if not strs:
                return -1

            print(strs,iteration,longelementlist)

            iteration = iteration+1


            lenlong,longestElement = counterFunct(strs)
            print(lenlong,longestElement)
            print("Iteration : " , iteration)


            if lenlong == 1 and not any(longestElement in string for string in longelementlist):
                return len(longestElement)

            elif any(longestElement in string for string in longelementlist):
                longelementlist.extend(  list(set(get_all_substrings(longestElement)))  )
                strsn = [element for element in strs if element != longestElement]                
                return uslen(strsn,iteration,longelementlist)
            
            
            else:

                
                longelementlist.extend(  list(set(get_all_substrings(longestElement)))  )

                print("Longelementlist : ", longelementlist)

                print("removing : " , longestElement)
                strsn = [element for element in strs if element != longestElement]

                return uslen(strsn,iteration,longelementlist)
                

        
        
        return uslen(strs,iteration,longelementlist)
