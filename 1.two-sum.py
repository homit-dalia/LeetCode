#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # first solution
        for i in range(len(nums)-1):

            for j in range(i+1,len(nums)):
                if(target == (nums[i] + nums[j])):
                    return [i,j]
                
        # other solution
        # doesnt work
        
        # for i in range(len(nums)):
        #     if i > target:
        #         continue
        #     diff = target - nums[i]
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         if nums[j] == diff:
        #             return [i,j] 


# @lc code=end

