'''You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"'''


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        # 1. find bulls count first by checking 1-1 index matches
        # 2. remaining indices of guess are potential cows (so find substring)
        # 3. Get the alpha: count matchs of cow indices in secret
        # 4. go through alphas in 2. and decrement counts in 3. until 0 and increment cow by 1 each time

        # count number of bulls
        guess_cow_ind = []
        secret_cow_char2count = {}

        bulls = 0
        for ind, num in enumerate(secret):
            if guess[ind]==secret[ind]:
                bulls+=1
            else:
                guess_cow_ind.append(ind)
                secret_cow_char2count[secret[ind]] = secret_cow_char2count.get(secret[ind],0) + 1
        
        
        cows = 0
        guess_cow = [guess[ind] for ind in guess_cow_ind]
        for key in guess_cow:
            if key in secret_cow_char2count and secret_cow_char2count[key] != 0:
                secret_cow_char2count[key]-=1
                cows+=1
        
        ans = '{}A{}B'.format(bulls, cows)
        return ans


            

            