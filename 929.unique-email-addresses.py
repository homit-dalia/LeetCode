#
# @lc app=leetcode id=929 lang=python
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        unique = set()

        for email in emails:
            local_email = ""
            em = str(email).split('@')
            em1 = em[0].split('+')
            for i in em1[0]:
                if(i!= '.'):
                    local_email = local_email + i
            local_email = local_email + "@" +em[1]
            unique.add(local_email)

        return len(unique)
    

# @lc code=end

