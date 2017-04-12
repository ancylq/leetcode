# coding:utf-8
'''
Given a string S, find the longest palindromic substring in S. You may 
assume that the maximum length of S is 1000, and there exists one 
unique longest palindromic substring.

Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example:
Input: "cbbd"
Output: "bb"

思路：b a b c d
     i j          判断i到j中间是不是回文
     i   j        判断i到j中间是不是回文
     i     j      判断i到j中间是不是回文
     i       j    判断i到j中间是不是回文
       i j        判断i到j中间是不是回文
       i   j      判断i到j中间是不是回文
       i     j    判断i到j中间是不是回文
     直到i到最后，并且j大于字符串长度结束


'''
class Solution(object):
    
    def isPalindrome(self, s, start, end):
        '''从两头向中间来判断是否为回文'''
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
         
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max, left, right = 0, 0, 0
        for i in range(len(s)):
            j = i+1
            while j < len(s):
                if self.isPalindrome(s, i, j):
                    if (j-i+1) > max:
                        left, right = i, j
                        max = j - i + 1
                j += 1
        print left, right, max
        return s[left:right+1]
            
if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome('babcd')