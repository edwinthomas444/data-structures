'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]


        dp[0][0] = True
        for i in range(1,len(s)+1):
            dp[i][0] = False
        # as first char is blank for s, the dp[0][j] would be same as dp[0][j-1] as blank as star is expanded as nothing and matches blank
        for j in range(1,len(p)+1):
            dp[0][j] = False if p[j-1]!='*' else dp[0][j-1]

        # print(dp, len(dp), len(dp[0]))
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*': # j-1 as dp is 1 indexed so in string jth index corr. to j-1st index
                    # if 0 occurences, then match with j-1 of pattern as if * didnt exist
                    # if 1 or more occurences then match with i-1 of string, as included for match
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j-1] == '?' or p[j-1] == s[i-1]: # i-1 and j-1 as 0 indexed but for dp we start with index 1
                    # if current matched, then copy previous also matched then only true
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        
        return dp[len(s)][len(p)]