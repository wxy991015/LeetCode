class TicTacToe:
    def __init__(self, n: int):
        self.board = []
        for i in range(n):
            self.board.append(n * [0])

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        # row check
        for i in range(len(self.board)):
            first = self.board[i][0]
            if first == 0: continue
            flag = True
            for j in range(1, len(self.board)):
                if self.board[i][j] != first:
                    flag = False
                    break
            if flag:
                return player
        
        # col check
        for j in range(len(self.board)):
            first = self.board[0][j]
            if first == 0: continue
            flag = True
            for i in range(1, len(self.board)):
                if self.board[i][j] != first:
                    flag = False
                    break
            if flag:
                return player
        
        # left diagonal check
        l_top = self.board[0][0]
        l_diagonal_check = True
        if l_top != 0:
            for i in range(1, len(self.board)):
                if self.board[i][i] != l_top:
                    l_diagonal_check = False
                    break
            if l_diagonal_check:
                return player

        # right diagonal check
        r_top = self.board[0][len(self.board)-1]
        r_diagonal_check = True
        if r_top != 0:
            for i in range(1, len(self.board)):
                if self.board[i][len(self.board)-i-1] != r_top:
                    r_diagonal_check = False
                    break
            if r_diagonal_check:
                return player
        return 0