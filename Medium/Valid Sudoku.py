from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    for i in range(len(board)):
        row_bucket = [0] * 9
        column_bucket = [0] * 9
        for j in range(len(board[i])):
            if board[i][j] != ".":
                row_bucket[ord(board[i][j])-"0"] += 1
                if row_bucket[ord(board[i][j]-"0")] > 1:
                    return False
                column_bucket[ord(board[j][i])-"0"] += 1
                if column_bucket[ord(board[j][i])-"0"] > 1:
                    return False
    left_diagonal = [0] * 9
    for i in range(len(board)):
        left_diagonal[ord(board[i][i])-"0"] += 1
        if left_diagonal[ord(board[i][i])-"0"] > 1:
            return False
    right_diagonal = [0] * 9
    for i in range(len(board)):
        right_diagonal[ord(board[i][len(board)-i-1])] += 1
        if right_diagonal[ord(board[i][len(board)-i-1])] > 1:
            return False
    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(f"Output: {isValidSudoku(board)}")