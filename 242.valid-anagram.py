#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len1 = len(s)
        len2 = len(t)

        if(len1 != len2):
            return False
        
        chars = [i for i in s]
        chars.sort()

        chars_2 = [i for i in t]
        chars_2.sort()

        if(chars != chars_2):
            return False
        
        return True
        


# @lc code=end

