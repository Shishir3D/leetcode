class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []

        def backtrack(opened, closed, sol):
            if closed >= n and opened >= n:
                ans = ''.join(sol)
                res.append(ans)
                return
            
            if opened < n:
                sol.append('(')
                backtrack(opened + 1, closed, sol[:])
                sol.pop()
            
            if closed < opened:
                sol.append(')')
                backtrack(opened, closed+1, sol[:])
                sol.pop()
            
        backtrack(0,0, [])
        return res
    