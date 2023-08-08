class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        len1 = len(nums1)
        len2 = len(nums2)
        if len1<len2:
            short = nums1
            long = nums2
        else :
            short = nums2
            long = nums1
        for i in range(len(short)):
            if short[i] in long:
                ans.append(short[i])
                long.remove(short[i])
        return ans
