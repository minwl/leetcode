class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        else:
            scount = {}
            tcount = {}
            for i in range(len(s)):
                scount[s[i]] = scount.get(s[i], 0) +1
                tcount[t[i]] = tcount.get(t[i], 0) +1

            return scount == tcount
            
