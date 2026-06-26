class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        q = deque()
        time = 0
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    count += 1
        
        while q and count>0:
            for _ in range(len(q)):
                r,c = q.popleft()
                directions = [(0,1),(1,0),(-1,0),(0,-1)]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    count -= 1
                    q.append((nr,nc))
            time += 1
                    
        if count == 0:
            return time
        return -1
                
