# 85 test cases passed

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        def uslen(strs):


            def get_max_str(lst):
                return max(lst, key=len)


            def counterFunct(s):

                counter = 0
                longestElement = get_max_str(s)

                for element in s:

                    if longestElement in element:
                        counter+=1
                return counter,longestElement



            lenlong,longestElement = counterFunct(strs)

            if lenlong == 1:
                return len(longestElement)
            else:
                strsn = [element for element in strs if element != longestElement]

                if strsn:
                    return uslen(strsn)
                else:
                    return -1
        
        
        return uslen(strs)
