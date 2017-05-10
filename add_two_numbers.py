# coding: utf-8
"""
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain 
a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

class ListNode(object):
    """
     Definition for singly-linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None
 
class Solution(object):
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if not l1 or not l2:
            return l2 if not l1 else l1
        carry = (l1.val + l2.val) / 10
        # result link
        res = ListNode((l1.val + l2.val) % 10)
        # store tmp res
        tmp_res = res
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            # add to link             
            tmp_res.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) / 10
            tmp_res = tmp_res.next
        # if l1 still left         
        while l1.next:
            l1 = l1.next
            tmp_res.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) / 10
            tmp_res = tmp_res.next
        # if l2 still left
        while l2.next:
            l2 = l2.next
            tmp_res.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) / 10
            tmp_res = tmp_res.next
        # if stall exist carry
        if carry != 0:
            tmp_res.next = ListNode(carry)
            tmp_res = tmp_res.next
        return res
        
class MySolution(object):
    """
    不符合题目规定的singly-linked list的结构，但也出了同样的结果。
    所以效率没测试。
    """
    def addTwoNumbers1(self, l1, l2):
        """
        没有考虑l1和l2不等长的情况。
        
        """
        if not l1 or not l2:
            return l2 if not l1 else l1
        num = 0
        result = []
        for i in range(len(l1)):
            
            total = l1[i] + l2[i] + num
            if total > 10:
                result.append(total%10)
                num = (l1[i] + l2[i]) / 10
            else:
                result.append(total)
                num = 0
            
        if num != 0:
            result.append(num)
            
        return result
        
    def addTwoNumbers2(self, l1, l2):
        """
        将l1和l2组合成数字做加法。不用考虑l1和l2不等长的情况
        """
        if not l1 or not l2:
            return l2 if not l1 else l1
        l1.reverse()
        l2.reverse()
        l1_num = int(''.join(map(str, l1)))
        l2_num = int(''.join(map(str, l2)))
        result = list(str(l1_num + l2_num))
        result.reverse()
        return result
        
if __name__ == '__main__':
    l1 = []
    l2 = [5, 6, 9, 2, 8]
    s = MySolution()
    print s.addTwoNumbers2(l1, l2)
