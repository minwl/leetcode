class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        pre = [1] * len(nums)
        sur = [1] * len(nums)
        prefix = surfix = 1
        for i in range(len(nums)):
            pre[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            sur[i] = surfix
            surfix *= nums[i]

        ans[0] = sur[0]
        ans[len(nums)-1] = pre[len(nums)-1]
        for i in range(1, len(nums)-1):
            ans[i] = pre[i]*sur[i]

        return ans

            

