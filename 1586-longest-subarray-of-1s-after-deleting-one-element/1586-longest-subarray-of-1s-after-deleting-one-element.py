class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = j = 0
        skip = 1
        maxlen = 0
        while j < len(nums):
            if nums[j] == 0:
                skip -= 1
            if skip < 0:
                if nums[i] == 0:
                    skip += 1
                i += 1
            j+=1
            maxlen = max(maxlen, j-i-1)
        
        return maxlen
