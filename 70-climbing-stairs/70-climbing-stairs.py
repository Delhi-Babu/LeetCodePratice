class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(target,n,count):
            if(n in memo):
                return memo[n]
            if n==target:
                return 1
            if n>target:
                return 0
            else:
                count += helper(target,n+1,count) + helper(target,n+2,count)
                memo[n]= count
                return count
            return 0
        return helper(n,0,0)