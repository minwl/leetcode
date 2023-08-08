class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct_s_t= {}
        dct_t_s={}
        ans = True
        for i in range(len(s)):
            if s[i] in dct_s_t:
                if t[i] != dct_s_t[s[i]]:
                    return False   
            else:
                dct_s_t[s[i]] = t[i]
        for i in range(len(s)):
            if t[i] in dct_t_s:
                if s[i] != dct_t_s[t[i]]:
                    return False   
            else:
                dct_t_s[t[i]] = s[i]            
                
        return ans