class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        
        dp1 = [0]*(n-1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0],nums[1])

        for i in range(2,n-1):
            notake = dp1[i-1]
            take = nums[i] + dp1[i-2]
            dp1[i] = max(take, notake)
        
        dp2 = [0]*(n-1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[1],nums[2])
        for i in range(2,n-1):
            notake = dp2[i-1]
            take = nums[i+1] + dp2[i-2]
            dp2[i] = max(take, notake)
        
        return max(dp1[n-2],dp2[n-2])
