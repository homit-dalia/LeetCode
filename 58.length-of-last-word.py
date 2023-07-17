#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        words = str(s).split(" ")
        print(words)
        i = len(words)-1
        while i >= 0:
            # print(words[i])
            if(words[i] != ""):
                return len(words[i])
            i-=1

# obj  = Solution() 
# print(obj.lengthOfLastWord(s= "   fly me   to   the moon  "))
# @lc code=end

