#
# @lc app=leetcode id=724 lang=python
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #this solution exceeded time limit for 732/746 case
        # left = 0
        # right = 0
        # index = -1

        # def sum(arr):
        #     sum = 0
        #     for j in range(len(arr)):
        #         sum += arr[j]
        #     return sum



        # for i in range(len(nums)):

        #     print("Summation of")

        #     print(str(nums[0:i]) + " " + str(nums[i+1:len(nums)]))

        #     left = sum(nums[0:i])
        #     right = sum(nums[i+1:len(nums)])

        #     print(str(left) + " " + str(right))

        #     if( left == right):
        #         print('Index Changed\n')
        #         index = i
        #         break
        # return index
    
        left = 0
        right = 0
        index = -1

        total = sum(nums)

        for i in range(len(nums)):

            #print("Summation of")

            #print(str(nums[0:i]) + " " + str(nums[i+1:len(nums)]))

            left = sum(nums[0:i])
            # right = sum(nums[i+1:len(nums)])

            #print(str(left) + " " + str(right))

            if( left == (total - nums[i] - left)):
                #print('Index Changed\n')
                index = i
                break
        return index


# print(Solution().pivotIndex([1,7,3,6,5,6]))
# print("----------------------------------------------------------")
# print(Solution().pivotIndex([2,1,-1]))
# print("----------------------------------------------------------")
# print(Solution().pivotIndex([-1,-1,0,0,-1,-1]))
# @lc code=end

