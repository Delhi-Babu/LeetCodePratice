class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            binary = bin(i).replace('0b','')
            count=0
            for j in binary:
                if j=='1':
                    count+=1
            ans.append(count)
        return ans
    