# coding:utf-8
'''
Given an array of integers, every element appears twice except for one. 
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you 
implement it without using extra memory? 
'''
class Solution(object):
    def singleNumberMY(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1, len(nums), 2): # 不从0开始是为了防止越界
            if nums[i] != nums[i-1]:
                return nums[i-1]
        return nums[-1]
        
    def singleNumber(self, nums):
        """
        利用异或, A ^ A = 0
        (2^1^4^5^2^4^1) => ((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5
        """
        result = 0
        for n in nums:
            result ^= n
        return result
    
if __name__ == '__main__':
    nums = [1,1,2,2,3]
    s = Solution()
    print s.singleNumber(nums)