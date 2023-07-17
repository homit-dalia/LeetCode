#
# @lc app=leetcode id=392 lang=python
#
# [392] Is Subsequence
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_t = len(t)
        len_s = len(s)
        if(len_t < len_s):
            return False
        
        i,j = 0, 0

        while i < len_s and j < len_t:
            if s[i] == t[j]:
                i+=1
            j+=1

        if(i == len_s):
            return True
        return False


# @lc code=end

