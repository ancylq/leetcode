# coding:utf-8
'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh". 
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = list(s)
        str_list.reverse()
        return ''.join(str_list)
        
if __name__ == '__main__':
    s = Solution()
    print s.reverseString('hello')