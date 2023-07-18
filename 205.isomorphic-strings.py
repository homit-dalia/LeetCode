#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) != len(t)):
            return False

        hashST, hashTS = {}, {}

        for c1, c2 in zip(s,t):
            if((c1 in hashST and hashST[c1] != c2) or (c2 in hashTS and hashTS[c2] != c1)):
                return False
            hashST[c1] = c2
            hashTS[c2] = c1
        return True

        # hash_s = {}
        # hash_t = {}
        # for i in range(len(s)):
        #     hash_s[s[i]] = hash_s.get(s[i], 0) + 1
        #     hash_t[t[i]] = hash_t.get(t[i], 0) + 1

        # print(hash_s)
        # print(hash_t)
        # for key1, key2 in zip(hash_s, hash_t):
        #     print(key1, key2)
        #     print(hash_s[key1], hash_t[key2])

        #     if (int(hash_s[key1]) != int(hash_t[key2])):
        #         return False
        
        # return True

print(Solution().isIsomorphic("paper", "title"))
# @lc code=end

