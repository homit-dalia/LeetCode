#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        threshold = int(len(nums)/2) + 1
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        for key in count:
            if(count[key] >=threshold):
                return key
        

# @lc code=end

