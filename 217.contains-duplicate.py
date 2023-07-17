#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        unique = set()


        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i] == nums[j]):
        #             return True
        # return False

        for i in range(len(nums)):
            if(nums[i] not in unique):
                unique.add(nums[i])
            else:
                return True
        return False
        
# @lc code=end

