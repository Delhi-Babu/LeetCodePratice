class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []
        
        def generate(oc, cc):
            if oc == cc == n:
                ans.append(''.join(stack))
                return 
            if oc < n:
                stack.append('(')
                generate(oc+1, cc)
                stack.pop()
            if cc < oc:
                stack.append(')')
                generate(oc,cc+1)
                stack.pop()
        
        generate(0,0)
        return ans