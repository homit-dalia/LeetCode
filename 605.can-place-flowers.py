#
# @lc app=leetcode id=605 lang=python
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        count = 0

        if(len(flowerbed) >=2 and flowerbed[0] == 0 and flowerbed[1] == 0 ):
            flowerbed[0] = 1
            count+=1

        if(len(flowerbed) >=2 and flowerbed[-1] == 0 and flowerbed[-2] == 0):
            flowerbed[-1] = 1
            count+=1
        
        if(len(flowerbed) == 1 and flowerbed[0] == 0):
            return True


        print(flowerbed)
        print(count)
        for i in range(len(flowerbed)-3):

            if(flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0):
                count+=1
                flowerbed[i+1] = 1
        
        print(count)
        return True if count >= n else False
    
print(Solution().canPlaceFlowers([0,0,1,0,0], 1))
# @lc code=end

