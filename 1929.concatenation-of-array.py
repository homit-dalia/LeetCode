#
# @lc app=leetcode id=1929 lang=python
#
# [1929] Concatenation of Array
#

# @lc code=start
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for j in range(2):
            for i in range(len(nums)):
                ans.append(nums[i])
        return ans

# @lc code=end

