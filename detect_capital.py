# coding:utf-8
'''
Given a word, you need to judge whether the usage of capitals in it is
right or not.

We define the usage of capitals in a word to be right when one of the 
following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital if it has more than 
    one letter, like "Google".
'''
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word is not None and ( \
               word.isupper() or \
               word.islower() or \
               (word[0].isupper() and word[1:].islower()))
            
    
if __name__ == '__main__':
    word = 'USA'
    s = Solution()
    print s.detectCapitalUse(word)