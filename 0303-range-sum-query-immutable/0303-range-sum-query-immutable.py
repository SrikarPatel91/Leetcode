class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.res=[0]*len(nums)
        self.res[0]=nums[0]
        for i in range(1,len(nums)):
            self.res[i]=self.res[i-1]+nums[i]
        # print(self.res)

    def sumRange(self, l: int, r: int) -> int:
        if l==0:
            return self.res[r]
        return self.res[r]-self.res[l-1]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)