'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true'''

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = len(s)
        if count==0:
            return True
        elif len(t)==0:
            return False

        i = 0
        for j in range(len(t)):
            if s[i]==t[j]:
                count-=1
                i+=1
            if i==len(s):
                break
        if count==0:
            return True
        return False


