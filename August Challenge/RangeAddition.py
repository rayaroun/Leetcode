#this approach doesn't get accepted before uses too much memory

from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        

        if not ops:
            return m*n

        res = [ [ 0 for i in range(n) ] for j in range(m) ]

        # print(res)


        def increment(x): 
            
            for i in range(x[0]):
                for j in range(x[1]):
                    res[i][j] += 1


        def findMaxVal():
            maxi = -1
            maxval = 0
            for i in range(m):
                for j in range(n):
                    if res[i][j] > maxi:
                        maxi = res[i][j]
            for i in range(m):
                for j in range(n):
                    if res[i][j] == maxi:
                        maxval+=1
            return maxval


        for element in ops:
            increment(element)

        # maxval = findMax()

        print(res)

        return findMaxVal()
