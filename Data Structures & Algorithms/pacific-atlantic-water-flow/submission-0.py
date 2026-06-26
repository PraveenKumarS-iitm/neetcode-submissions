class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            
            while q:
                r,c = q.popleft()

                directions = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr,dc in directions:
                    nr , nc = r + dr, c + dc
                    if (
                        nr < 0 or nc < 0 or
                        nr >= rows or nc >= cols or
                        (nr, nc) in visited or
                        heights[nr][nc] < heights[r][c]
                    ):
                        continue

                    visited.add((nr, nc))
                    q.append((nr, nc))
            return visited
        
        pacific = []
        atlantic = []

        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((rows-1,c))
        for r in range(rows):
            pacific.append((r,0))
            atlantic.append((r, cols-1))
        
        pac = bfs(pacific)
        atl = bfs(atlantic)

        return [[r,c] for r,c in pac & atl]
