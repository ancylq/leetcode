# coding: utf-8
"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2 
"""
class Solution_good(object):
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, num, target):
        # sort
        sorted_num = sorted(num)

        # two points
        left = 0
        right = len(num) - 1
        res = []
        while (left < right):
            sum = sorted_num[left] + sorted_num[right]
            if sum == target:
                # find out index
                break;
            elif sum > target:
                right -= 1
            else:
                left += 1

        if left == right:
            return -1, -1
        else:
            pos1 = num.index(sorted_num[left]) + 1
            pos2 = num.index(sorted_num[right]) + 1
            if pos1 == pos2:    # find again
                pos2 = num[pos1:].index(sorted_num[right]) + pos1 + 1

            return min(pos1, pos2), max(pos1, pos2)


class Solution_better(object):
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        """
        采用hashtable 将数值即为key value为index 将target-num[index]作为搜索条件
        
        散列表（Hash table，也叫哈希表），是根据关键码值(Key value)而直接进行访问的数据结构。
        也就是说，它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。
        这个映射函数叫做散列函数，存放记录的数组叫做散列表。
        """
        process = {}
        for i in range(len(nums)):
            if target-nums[i] in process:
                return [process[target-nums[i]]+1, i+1]
            else:
                process[nums[i]] = i

s = Solution_good()
# s = Solution_better()
print s.twoSum([2, 7, 11, 15], 9)