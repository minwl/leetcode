class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:        
        dic = Counter(nums)
        for k in dic.keys():
            if dic[k] > 1:
                return True