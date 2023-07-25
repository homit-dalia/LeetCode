#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        ans = []

        for i, n in enumerate(nums):
            count[n] = count.get(n, 0) + 1

        print(count)
        for i, n in enumerate(count):
            frequency[count[n]].append(n)

        print(frequency)
        for i in range(len(frequency)-1, 0, -1):
            for j in frequency[i]:
                ans.append(j)
                if(len(ans) == k):
                    #ans.sort()
                    return ans



print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))
        
# @lc code=end

