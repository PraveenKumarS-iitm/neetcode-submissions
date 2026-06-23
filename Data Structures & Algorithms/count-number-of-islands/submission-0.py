class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>= cols or grid[r][c] == '0' or (r,c) in visited:
                return
            visited.add((r,c))

            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            for dr,dc in directions:
                nr,nc = r + dr, c + dc
                dfs(nr,nc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count += 1
                    dfs(r,c)
        
        return count