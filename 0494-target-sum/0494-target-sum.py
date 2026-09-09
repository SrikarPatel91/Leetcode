class Solution(object):
    def findTargetSumWays(self, arr, diff):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans=abs(sum(arr)+diff)
        if ans%2==1 or sum(arr)<abs(diff):
            return 0
        ans//=2
        dp=[[-1]*(ans+1) for _ in range(len(arr)+1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if j==0 and i==0:
                    dp[i][j]=1
                elif i==0:
                    dp[i][j]=0
                elif j<arr[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
        return dp[-1][-1]
        