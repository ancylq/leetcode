# coding:utf-8
'''
Given a positive integer, output its complement number. The complement 
strategy is to flip the bits of its binary representation.

Note:
    The given integer is guaranteed to fit within the range of a 32-bit 
    signed integer.
    You could assume no leading zero bit in the integer’s binary 
    representation.

Example 1:
    Input: 5
    Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero 
    bits), and its complement is 010. So you need to output 2.

Example 2:
    Input: 1
    Output: 0
    Explanation: The binary representation of 1 is 1 (no leading zero 
    bits), and its complement is 0. So you need to output 0.
'''
class Solution(object):
    '''score:35.61'''
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        或 int(''.join(str(1 - int(x)) for x in bin(num)[2:]), 2) # 52.39
        """
        quotient = num
        result = ''
        while quotient >= 1:
            quotient, remainder = divmod(quotient, 2)
            if remainder == 1:
                result = '0' + result
            else:
                result = '1'+ result
        print result
        return int(result, 2)
    
class SolutionBest(object):
    '''score:91.76'''
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            num ^= i
            print num
            i <<= 1
        return num

if __name__ == '__main__':
    s = SolutionBest()
    print s.findComplement(5)