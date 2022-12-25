'''Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_elem = set()
        count = 0
        for char in s:
            if char in unique_elem:
                # when same character encountered more than once it can be part of
                # first and last segment of the palindrome
                count+=2
                unique_elem.remove(char)
            else:
                unique_elem.add(char)
        if len(unique_elem):
            count+=1
        
        return count