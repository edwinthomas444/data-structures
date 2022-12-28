'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1'''

# logic:
# dfs from every i,j thats not visited
# mark visited nodes in each dfs call
class Solution(object):
    def isvalid(self, rows, cols, i, j):
        if i>=0 and j>=0 and i<rows and j<cols:
            return True
        return False

    def dfs(self, root, visited, rows, cols):
        
        r, c = root
        # making grid value '0' so that i,j wont count it as an additional connected component
        visited[r][c] = '0'
        neigbours = [(r, c+1),
                     (r+1, c),
                     (r-1, c),
                     (r, c-1)]
        for n_hop in neigbours:
            rc, cc = n_hop
            if self.isvalid(rows, cols, rc, cc) and visited[rc][cc]=='1':
                self.dfs(n_hop, visited, rows, cols)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    # each connected component
                    count+=1
                    self.dfs((i,j), grid, rows, cols)
        return count
        