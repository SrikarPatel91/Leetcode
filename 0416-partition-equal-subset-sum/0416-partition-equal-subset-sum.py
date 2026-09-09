class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        sol=sum(arr)
        if sol%2==1:
            return False
        sol//=2
        dp=[[-1]*(sol+1) for _ in range(len(arr)+1)]
        # def solve(i,sol):
        #     if sol==0:
        #         return True
        #     if i==0:
        #         return False
        #     if dp[i][sol]!=-1:
        #         return dp[i][sol]
        #     if sol<arr[i-1]:
        #         dp[i][sol]=solve(i-1,sol)
        #     else:
        #         dp[i][sol]=solve(i-1,sol) or solve(i-1,sol-arr[i-1])
        #     return dp[i][sol]
        # return solve(len(arr),sol)
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if j==0:
                    dp[i][j]=True
                elif i==0:
                    dp[i][j]=False
                # if dp[i][j]!=-1:
                    # return dp[i][j]
                elif j<arr[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
        return dp[-1][-1]