class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #all regions that are 4-directionally surrounded by X
        #are captured and should be changed to X
        #any regions that are not 4-directionally surrounded by X
        #are not captured and should not be changed
        if not board or not board[0]:
            return
        #use DFS
        #find all O's on the edges
        stack = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i in (0, len(board)-1) or j in (0, len(board[0])-1):
                    if board[i][j] == 'O':
                        stack.append((i,j))
        #mark all O's connected to the edges as safe
        while stack:
            row, col = stack.pop()
            board[row][col] = 'S'
            for r, c in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'O':
                    stack.append((r,c))
        #change all remaining O's to X
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        #change all S's back to O's
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
    
