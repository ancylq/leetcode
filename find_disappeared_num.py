# coding:utf-8
'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some 
elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume 
the returned list does not count as extra space.

Example:
    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [5,6]
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        origin = [0] * len(nums)
        for n in nums:
            origin[n-1] = 1
        return [i+1 for i, v in enumerate(origin) if v == 0]
    
if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    s = Solution()
    print s.findDisappearedNumbers(nums)
