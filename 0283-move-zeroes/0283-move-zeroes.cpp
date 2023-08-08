class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
        int n = nums.size();
        int i, j;
        i = 0;
        j = 0;
        for (i; i<n; i++){
            if (nums[i] != 0){
                int temp = nums[j];
                nums[j]= nums[i];
                nums[i] = temp;
                j++;
            }
        }
    }
};
