# Initial Draft - 50 test cases passed out of about a 100

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def get_max_str(lst):
            return max(lst, key=len)


        counter = 0
        longestElement = get_max_str(strs)

        for element in strs:

            if longestElement in element:
                counter+=1
            

        if counter == 1:
            return len(longestElement)
        else:
            return -1
          
  
