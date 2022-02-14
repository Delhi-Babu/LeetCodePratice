class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        def helper(row,col, grid, count):
            if f"{row},{col}" in memo:
                return memo[f"{row},{col}"]
            if(row == len(grid)-1 and col == len(grid[0])-1):
                return grid[row][col]
            elif(row > len(grid)-1 or col > len(grid[0])-1):
                return float("inf")
            else:
                down = helper(row+1,col,grid,count)
                right = helper(row,col+1,grid,count)
                count = grid[row][col] + min(down,right)
                memo[f"{row},{col}"] = count
                return count
        
        return helper(0,0,grid,0)