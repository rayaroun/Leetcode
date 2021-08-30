#thought up a different way of doing it. Managed to trick 23 out of 60is test cases into passing before the bluff was called

from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:

        if not ops:
            return m*n

        min = m*n

        for element in ops:
            temp = element[0] * element[1]
            if temp < min:
                min = temp
        
        return min
