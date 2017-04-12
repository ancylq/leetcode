#coding:utf-8
"""
Given a string, find the length of the longest substring without 
repeating characters. For example, the longest substring without 
repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.
"""
class Solution:  
    # @return an integer  
    def lengthOfLongestSubstring(self, s):
        res = 0
        left = 0
        d = {}

        for i, ch in enumerate(s):
            if ch in d and d[ch] >= left:
                left = d[ch] + 1
            d[ch] = i
            res = max(res, i - left + 1)
        return res  