
'''Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".'''


# 3 solutions, bottom-up DP, 
# top-down memoization and 
# top-down recursive(no memoization) are implemented
class Solution(object):
    def isMatch_bottomup_DP(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        pattern_len = len(p)
        string_len = len(s)

        # dp: bottom-up approach
        
        dp = [[None for _ in range(pattern_len+1)] for _ in range(string_len+1)]

        dp[0][0] = True
        for i in range(1, string_len+1):
            dp[i][0] = False
        for j in range(1, pattern_len+1):
            # basically '' matches with single char followed by * , so these cases are considered bellow and for * location
            # simply previous one is repeated..
            if (j<pattern_len and p[j] == '*') or p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = False 

        for i in range(1, string_len+1):
            for j in range(1, pattern_len+1):
                if p[j-1] == '*':
                    # as j-1 already computes for char* as one unit, we can skip when * appears
                    dp[i][j] = dp[i][j-1]
                    continue

                matched = s[i-1] == p[j-1] or p[j-1] == '.'
                if j<pattern_len and p[j] == '*':
                    dp[i][j] = dp[i][j-1] or (matched and dp[i-1][j])
                elif matched:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        
        return dp[string_len][pattern_len]

    def isMatch_topdown_memoization(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        pattern_len = len(p)
        string_len = len(s)

        # top-down memoization
        cache = {}

        def dfs(i,j):
            # if element is there in cache just return from the cache
            if (i,j) in cache:
                return cache[(i,j)]

            # when j exceeds pattern and i exceeds string length return true
            if j>=pattern_len and i>=string_len:
                return True
            # when j exceeds pattern length but i is till in between string, means no matches found , return false
            if j>=pattern_len and i<string_len:
                return False
            
            # all below cases are when j<pattern_length and i can be greater or lesser than string length
            # note: p[j] would never be a * as character comes first and we skip j by 0 or 2 pts..
            match = i<string_len and ((s[i] == p[j]) or p[j] == '.')
            
            if j+1<pattern_len and p[j+1] == "*":
                # assume j is pointing to first char in 'a*' , then first case is we repeat a 0 times.
                # and see if match is there after j+2 (or after a*)
                # second case, is char at j matched with i, and we keep j but move i by one 
                # (so that j can again repeat 0 or more times)
                cache[(i,j)] = dfs(i, j+2) or (match and dfs(i+1, j))
                return cache[(i,j)]
            
            # if matched, then move both by 1
            if match:
                cache[(i,j)] = dfs(i+1, j+1) 
                return cache[(i,j)]

            # all other cases: includes when no match for i and j return False
            cache[(i,j)] = False
            return  cache[(i,j)]
        
        return dfs(0,0)

    def isMatch_topdown_nomemoization(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        pattern_len = len(p)
        string_len = len(s)

        def dfs(i,j):
            # when j exceeds pattern and i exceeds string length return true
            if j>=pattern_len and i>=string_len:
                return True
            if j>=pattern_len and i<string_len:
                return False
            
            # note: p[j] would never be a * as character comes first and we skip j by 0 or 2 pts..
            match = i<string_len and ((s[i] == p[j]) or p[j] == '.')
            
            if j+1<pattern_len and p[j+1] == "*":
                # assume j is pointing to first char in 'a*' , then first case is we repeat a 0 times.
                # and see if match is there after j+2 (or after a*)
                # second case, is char at j matched with i, and we keep j but move i by one 
                # (so that j can again repeat 0 or more times)
                return dfs(i, j+2) or (match and dfs(i+1, j))
            
            # if matched, then move both by 1
            if match:
                return dfs(i+1, j+1)

            # all other cases: includes when no match for i and j return False
            return False
        
        return dfs(0,0)

            
