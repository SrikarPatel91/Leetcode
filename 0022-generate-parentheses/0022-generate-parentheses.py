class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def sol(i,j,a):
            if len(a)==n*2:
                res.append(a)
                return
            if i<n:
                sol(i+1,j,a+"(")
            if j<i:
                sol(i,j+1,a+")")
        sol(0,0,"")
        return res