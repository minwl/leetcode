class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int ans = 0;
        vector<int> ansvec = {};
        for (int i = 0; i < nums.size(); i++){
            ans += nums[i];
            ansvec.push_back(ans);   
        }
        return ansvec;
    }
};