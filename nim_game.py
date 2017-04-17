# coding:utf-8
'''
 You are playing the following Nim Game with your friend: There is a 
 heap of stones on the table, each time one of you take turns to 
 remove 1 to 3 stones. The one who removes the last stone will be the 
 winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. 
Write a function to determine whether you can win the game given the 
number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win 
the game: no matter 1, 2, or 3 stones you remove, the last stone will 
always be removed by your friend.

分析：
    1个石子，先手全部拿走；
    2个石子，先手全部拿走；
    3个石子，先手全部拿走；
    4个石子，后手面对的是先手的第1，2，3情况，后手必胜；
    5个石子，先手拿走1个让后手面对第4种情况，后手必败；
    6个石子，先手拿走2个让后手面对第4种情况，后手必败；
    7个石子，先手拿走3个让后手面对第4种情况，后手必败；
    8个石子，后手面对的是先手的第5,6,7情况，后手必胜；
    ……
容易看出来，只有当出现了4的倍数，先手无可奈何，其余情况先手都可以获胜。
（石子数量为4的倍数）后手的获胜策略十分简单，每次取石子的数量，与上一次先手取石子的数量和为4即可；
（石子数量不为4的倍数）先手的获胜策略也十分简单，每次都令取之后剩余的石子数量为4的倍数（4*0=0，直接拿光），他就处于后手的位置上，利用上一行的策略获胜。
'''
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        else:
            return True
