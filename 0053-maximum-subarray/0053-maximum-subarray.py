class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxval = nums[0]
        cursum = nums[0]
        for i in range(1, len(nums)):
            cursum = max(cursum + nums[i], nums[i])
            maxval = max(cursum, maxval)
        return maxval
