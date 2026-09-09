class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c=nums[0]
        maxi=nums[0]
        for  i in range(1,len(nums)):
            c=max(nums[i],c+nums[i])
            maxi=max(maxi,c)
        return maxi