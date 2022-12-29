'''There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
Example 1:


Input: m = 3, n = 7
Output: 28'''

class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # can be solved numerically
        # m-1 + n-1 string, how many permutations? each m-1 are R and each n-1 are D
        prod = 1
        for i in range(n, n+m-1):
            prod*=i
            prod//=i-n+1 # this will go from m-1 to 1  as i-n+1  is n-(n+m-1) = m-1, then m-2
        return prod

