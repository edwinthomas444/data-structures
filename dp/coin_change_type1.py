'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dont need 2d array for this problem
        target_sum = amount
        n = len(coins)
        dp = [1e08 for j in range(target_sum + 1)]
 
        # 0 coins needed for 0
        dp[0] = 0
        for j in range(target_sum+1):
            min_val = 1e08
            # min among subtracting all coin possiblities from current sum
            for i in range(1, n+1):
                if j - coins[i - 1] >= 0:
                    # Add the number of ways to make change using the current coin
                    dp[j] = min(1+dp[j - coins[i - 1]], dp[j])
        
        # print(dp)
        if dp[-1] == 1e08:
            return -1
            
        return dp[-1]
