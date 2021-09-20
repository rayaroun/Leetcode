'''

Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit

Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag

 

Constraints:

    1 <= s.length, t.length <= 1000
    s and t consist of English letters.




'''






from typing import DefaultDict
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        
        if M < N:
            return 0
        if M == N:
            return int(s == t)
        
        # dp[i] is the number of distinct subsequences of s which equal t[:i] so far
        dp = [0] * (N + 1)
        dp[0] = 1

        # tis[ch] is the list of all indices i s.t. t[i] == ch
        tis = DefaultDict(list)
        for i in range(N - 1, -1, -1):
            ch = t[i]
            tis[ch].append(i)
        
        for ch in s:
            for ti in tis[ch]:
                dp[ti + 1] += dp[ti]
        
        return dp[N]

