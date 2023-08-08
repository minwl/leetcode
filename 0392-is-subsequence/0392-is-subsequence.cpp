class Solution {
public:
    bool isSubsequence(string s, string t) {
        int lenT=t.size();
        int lenS=s.size();
        if(lenT<lenS){
            return false;
        }
        int i = 0;
        int j = 0;
        while (i < lenS and j < lenT){
            if (s[i]==t[j]){
                i++;
            }
            j++;
        }
    return (i == lenS);
    }
};