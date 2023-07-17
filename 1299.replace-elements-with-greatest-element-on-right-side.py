#
# @lc app=leetcode id=1299 lang=python
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # great_arr = []

        # def find_greatest(list1):


        #     greatest = -1
        #     for i in range(len(list1)):
        #         if(list1[i] > greatest):
        #             greatest = list1[i]

        #     return greatest
        
        # new_arr = []
        # length = len(arr)
        # for i in range(len(arr)):
            
        #     if(great_arr[i] == arr[i+1]):

        #     great = find_greatest(arr[i+1:length])
        #     great_arr.append(great)

        #     new_arr.append()
        
        # return new_arr
        
        greatest = -1
        new_arr = [-1]
        for i in range(len(arr)-1, 0, -1):
            if(arr[i] > greatest):
                greatest = arr[i]
            new_arr.append(greatest)
        new_arr.reverse()
        return new_arr
# @lc code=end

