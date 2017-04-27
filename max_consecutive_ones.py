# coding:utf-8
'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
'''
class Solution(object):
    def findMaxConsecutiveOnesMy(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        new_len = 0
        for n in nums:
            if n == 1:
                max_len+=1
            else:
                new_len = self.findMaxConsecutiveOnesMy(nums[max_len+1:])
                break
        if max_len < new_len:
            max_len = new_len
        return max_len
    
    def findMaxConsecutiveOnes(self, nums):
        ans = cnt = 0
        for n in nums:
            if n == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans
    
if __name__ == '__main__':
    bin_list = [1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1]
    s = Solution()
    print s.findMaxConsecutiveOnes(bin_list)