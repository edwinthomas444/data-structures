'''You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.'''


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        count = {}
        l = 0

        result = 0

        max_f = 0
        for r in range(0,len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            # keep track of maximum frequency element
            max_f = max(max_f, count[s[r]]) # as the rth character could be the most new freqeunt element

            # move left pointer in case condition on k doesnt hold
            while (r-l+1)-max_f > k:
                # update count of left most character (decrement it as we move by one point)
                count[s[l]]-=1
                # increment l
                l+=1
                # note: after l moves, max_f can only decrease or stay constant
                # so the window_size-max_f will only be lesser greater than before value
                # which is constrained by k
                # but if max_f increases, we can also have a potentially larger window_size so that 
                # window_size-max_f will be lesser than k again and result will change as window_size increased.
                # so it is okay to overestimate max_f (i.e not decrement max_f) as the results wont change any way
                
            result = max(r-l+1, result)
        
        return result