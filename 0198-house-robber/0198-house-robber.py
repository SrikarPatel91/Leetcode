class Solution:
    def rob(self, nums: List[int]) -> int:
        # def rec(i,picked):
        #         if i==len(nums): return 0
        #         if picked==1:return rec(i+1,0)
        #         return max(nums[i]+rec(i+1,1),rec(i+1,0))

        dp=[[0]*2 for _ in range(len(nums)+1)]
        for i in range(1,len(dp)):
            dp[i][0]=max(dp[i-1][1]+nums[i-1],dp[i-1][0])
            dp[i][1]=dp[i-1][0]
        return max(dp[-1][0],dp[-1][-1])