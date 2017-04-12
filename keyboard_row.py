# coding:utf-8
'''
Given a List of words, return the words that can be typed using letters 
of alphabet on only one row's of American keyboard

Example 1:
    Input: ["Hello", "Alaska", "Dad", "Peace"]
    Output: ["Alaska", "Dad"]

Note:
    You may use one character in the keyboard more than once.
    You may assume the input string will only contain letters of alphabet.
'''
class Solution(object):
    '''score:49.82'''
    KEYBORD_ROW = ['qwertyuiopQWERTYUIOP',
                   'asdfghjklASDFGHJKL',
                   'zxcvbnmZXCVBNM']
    
    def isOnRow(self, word, keybord):
        for w in word:
            if w not in keybord:
                return False
        return True
                
    
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for word in words:
            for keybord in self.KEYBORD_ROW:
                if word[0] in keybord:
                    if self.isOnRow(word, keybord):
                        result.append(word)
                        break
        return result
    
if __name__ == '__main__':
    s = Solution()
    print s.findWords(["Hello", "Alaska", "Dad", "Peace"])