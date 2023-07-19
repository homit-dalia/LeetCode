#
# @lc app=leetcode id=496 lang=python
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in range(len(nums1)):
            greatest = -1
            found = False
            for j in range(len(nums2)):

                if(nums2[j] == nums1[i]):
                    found = True
                if(found):
                    if (nums2[j] <= nums1[i]):
                        continue
                    greatest = nums2[j]
                    break
                else:
                    continue
            arr.append(greatest)
        
        return arr


            

            

            
        
# @lc code=end

