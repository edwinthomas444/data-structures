'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        d_u = {x:0 for x in p}
        for x in p:
            d_u[x]+=1

        i=0
        ans = []
        m = len(s)
        n = len(p)

        d_window = {}
        for i in range(0, len(s)-len(p)+1):
            
            if i==0:
                window = s[:n]
                for char in window:
                    d_window[char]=1 if char not in d_window else d_window[char]+1
            else:
                d_window[s[i-1]]-=1
                d_window[s[i+n-1]] = 1 if s[i+n-1] not in d_window else d_window[s[i+n-1]]+1

            found = True
            # check if anagram
            for key in d_u:
                val = -1 if key not in d_window else d_window[key]
                if d_u[key]!=val:
                    found = False
                    break

            if found:
                ans.append(i)
            
        return ans