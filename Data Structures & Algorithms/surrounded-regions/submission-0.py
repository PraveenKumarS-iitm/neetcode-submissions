class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows-1 or c == cols - 1) and board[r][c] == 'O':
                    q.append((r,c)) 
                    board[r][c] = 'S'
        
        while q:
            r,c = q.popleft()

            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] == 'O':
                    board[nr][nc] = 'S'
                    q.append((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'