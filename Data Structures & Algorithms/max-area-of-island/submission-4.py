class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxarea = 0
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            area = 1

            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            for dr,dc in directions:
                nr,nc = dr + r, c + dc
                area += dfs(nr,nc)
            return area
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxarea = max(maxarea,dfs(r,c))
        return maxarea
        
        # def bfs(r,c):
        #     q = deque()
        #     q.append((r,c))
        #     visited.add((r,c))
        #     area = 0

        #     while q:
        #         r,c = q.popleft()
        #         area += 1

        #         directions = [(0,1),(1,0),(0,-1),(-1,0)]

        #         for dr,dc in directions:
        #             nr, nc = r + dr, c + dc

        #             if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 and (nr,nc) not in visited:
        #                 visited.add((nr,nc))
        #                 q.append((nr,nc))
        #     return area
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1 and (r,c) not in visited:
        #             maxarea = max(maxarea, bfs(r,c))
        # return maxarea
        