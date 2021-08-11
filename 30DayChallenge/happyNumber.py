"""

Write an algorithm to determine if a number n is happy.


A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
 82 (81 + 1)
 68 (64 + 4)
 100 (36 + 64)
 1 (1 + 0 + 0)


Example 2:

Input: n = 2
Output: false

 

Constraints:

    1 <= n <= 231 - 1



"""


import math

class Solution:
    def isHappy(self, n: int):
        
        
        if n == 1:
            return True

        
        if n < 10 and n != 7:
            return False
        
        else:

            sqsum=0
            len_n = int(len(str(n)))

            

            for i in range(1, len_n + 1):
                sqsum = sqsum + pow(n%10,2)
                n = math.floor(n/10)

            return self.isHappy(self,n=sqsum)
