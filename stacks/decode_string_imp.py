'''Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"'''

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if char!=']':
                stack.append(char)
            else:                
                sub_str = ''
                while stack[-1]!='[':
                    sub_str = stack.pop() + sub_str
                # pop the [ bracket, note: [[c]] not possible (no redundant brackets)

                stack.pop()

                digit = ''
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                
                # important to append back solution of sub problem to the original stack list
                stack.append(int(digit)*sub_str)
        
        return ''.join(stack)