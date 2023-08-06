class Solution {
public:
    int maxVowels(string s, int k) {
        int j=0;
        int n = s.size();
        
        int count=0;
        while(j<k){
            if ((s[j]=='a')|(s[j]=='e')|(s[j]=='i')|(s[j]=='o')|(s[j]=='u'))
            count++;
            j++;
        }
        int maxcount = count;
         while(j<n){
            if ((s[j-k]=='a')|(s[j-k]=='e')|(s[j-k]=='i')|(s[j-k]=='o')|(s[j-k]=='u')) count--;
            if ((s[j]=='a')|(s[j]=='e')|(s[j]=='i')|(s[j]=='o')|(s[j]=='u'))
            {
                count++;
                if(count>maxcount) maxcount=count;
            }
            j++;

         }



    return maxcount;
    }
};


//         while(j<n){
        //     if ((s[j]=='a')|(s[j]=='e')|(s[j]=='i')|(s[j]=='o')|(s[j]=='u')){count++;}
        //     if(j-i<k-1) {
        //         ++j;
        //     }
        //     else if (j-i==k-1) {
                
        //         if(count>maxcount) maxcount=count;
        //         if ((s[i]=='a')|(s[i]=='e')|(s[i]=='i')|(s[i]=='o')|(s[i]=='u')){count--;}
        //         i++;
        //         j++;
        //         count=0;
        //     }
            
        // } return maxcount;


