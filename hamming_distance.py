# coding:utf-8
'''
The Hamming distance between two integers is the number of positions at
which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31. 

Example:
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

对两个字符串进行异或运算，并统计结果为1的个数，那么这个数就是汉明距离。
换句话说，它就是将一个字符串变换成另外一个字符串所需要替换的字符个数。
例如：
1011101 与 1001001 之间的汉明距离是 2。
2143896 与 2233796 之间的汉明距离是 3。
"toned" 与 "roses" 之间的汉明距离是 3。
'''
class Solution(object):
    '''按题目的意思是求二进制数的汉明距离'''
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x ^ y
        result = 0
        for i in range(32):
            result += (n>>i)&1
        return result
        
if __name__ == '__main__':
    s = Solution()
    print s.hammingDistance(1, 4)