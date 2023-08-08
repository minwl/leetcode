int maxOperations(int* nums, int numsSize, int k){

    //Q. sort 안하고 풀수있는 방법?

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

qsort(nums,numsSize, sizeof(int), cmpfunc);

int i = 0, j = numsSize-1, count=0;

while(i<j){
    if (nums[i]+nums[j] > k) j--;
    else if (nums[i]+nums[j] < k) i++;
    else{
        count++;
        i++;
        j--;
    }
}

return count;
}