class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = dict()
        for i, n in enumerate(nums):
            sub = target-n
            if sub in dct:
                return [dct[sub], i]
            else:
                dct[n] = i