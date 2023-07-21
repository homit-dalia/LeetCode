#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = str(s).split(" ")
        if(len(pattern) != len(s)):
            return False

        mapP = {}
        mapS = {}
        map_items = {}

        for i in range(len(pattern)):
            mapP[i] = pattern[i]
            mapS[i] = s[i]

        for i in range(len(pattern)):
            if(mapP[i] in map_items and mapS[i] != map_items[mapP[i]]):
                #write code
                return False
            else:
                map_items[mapP[i]] = mapS[i]
        
        print(mapP)
        print(mapS)
        print(map_items)
        return False if (len(map_items) != len(set(list(map_items[i] for i in map_items)))) else True

print(Solution().wordPattern(pattern = "aaaa", s = "dog cat cat dog"))    
# @lc code=end

