#
# @lc app=leetcode id=1189 lang=python
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        map = {}
        count = 0
        for i, n in enumerate(text):
            map[n] = map.get(n, 0) + 1        

        print(map)

        while([map[i] for i in "balloon"] > 0):
            map[i] = - [map[i] for i in "balloon"]
        
        return count


print(Solution().maxNumberOfBalloons("loonbalxballpoon"))


# @lc code=end

