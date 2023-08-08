class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flip = k
        i = j = 0
        maxlen = 0
        while j < len(nums):
            if nums[j] ==0:
                flip -= 1                
            if flip < 0:
                if nums[i] == 0:
                    flip += 1
                i += 1
            j += 1
            maxlen = max(j-i, maxlen)
        return maxlen