#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        if (numRows == 1):
            return [[1]]
        elif (numRows == 2):
            ans.append([1])
            ans.append([1,1])
            return ans
        else:
            ans.append([1])
            ans.append([1,1])

        for i in range(3, numRows+1):
            num_add = i - 2
            local_add = []
            local_add.append(1) #0 th value
            for j in range(num_add):
                #print("Local Append ")
                local_add.append(ans[i-2][j] + ans[i-2][j+1])
                #print(local_add)
            local_add.append(1) # i'th value
            ans.append(local_add)
            #print(f"Global Ans, after i  {str(i)}")
            #print(ans)

        return ans

# obj = Solution()
# obj.generate(5)
# @lc code=end

