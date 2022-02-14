class Solution:
    # not a best solution see neetcode
    def helper(self,matrix,i,j,res):
        if i < 0 or i >= len(matrix) or j < 0 or j>=len(matrix[0]) or matrix[i][j] == '#':  return

        res.append(matrix[i][j])
        matrix[i][j] = '#'


        if j>=i or i == j+1:
            self.helper(matrix,i,j+1,res)
        self.helper(matrix,i+1,j,res)
        self.helper(matrix,i,j-1,res)
        self.helper(matrix,i-1,j,res)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = [] 
        self.helper(matrix,0,0,res)
        return res
            
        