int longestSubarray(int* nums, int numsSize){
    int i = 0;
    int j = 0;
    int k = 1;
    int maxlen = 0;

    while (j < numsSize){
        if (nums[j] == 0) k--;
        if (k < 0){
            if (nums[i] == 0) k++;
            i++;
        }
        j++;
        maxlen = fmax(maxlen, j-i-1);
    }
    return maxlen;

}