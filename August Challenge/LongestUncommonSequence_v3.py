#94 Test cases passed out of 98 with the script

from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
        longelementlist = []
        iteration = 0
        
        def get_max_str(lst):
            return max(lst, key=len)

        

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
                longelementlist.append(longestElement)
                strsn = [element for element in strs if element != longestElement]                
                return uslen(strsn,iteration,longelementlist)
            
            
            else:

                
                longelementlist.append(longestElement)

                print("Longelementlist : ", longelementlist)

                print("removing : " , longestElement)
                strsn = [element for element in strs if element != longestElement]

                return uslen(strsn,iteration,longelementlist)
                

        
        
        return uslen(strs,iteration,longelementlist)
