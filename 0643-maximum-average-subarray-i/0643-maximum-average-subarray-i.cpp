class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int i = 0, j = 0;
        int n = nums.size();
        double maxavg=-INFINITY;
        double sum = 0;
        while (j < n){
            sum += nums[j];
            if (j-i<k-1) j++;
            else if(j-i==k-1){
                double avg = sum/k;
                if (avg>maxavg) maxavg = avg;
                sum-=nums[i];
                i++;
                j++;
            }
        } return maxavg;
    }};
        








//         while(p <= n-k){

//             double sum = 0;
//             for (int i = 0; i < k; i++){
//                 sum += nums[i+p];
//             }
//             double avg = sum/k;

//             if(avg > maxavg) maxavg = avg;
//             p++;
//         }
//         return maxavg;
//     }
// };