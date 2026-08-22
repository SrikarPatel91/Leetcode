class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        i=1
        j=max(piles)
        if len(piles)==h:
            return j
        while i<=j:
            mid=(i+j)//2
            res=0
            # flag=True
            for p in piles:
                res+=p//mid
                if p%mid!=0:
                    res+=1
                if res>h:
                    # flag=False
                    # i=mid+1
                    break
                
            if res>h:
                i=mid+1
            else:
                j=mid-1
            # print(i,j,mid,res)

        return i