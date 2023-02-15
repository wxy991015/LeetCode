from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    # row check
    for i in range(len(board)):
        row_bucket = [0] * 9
        for j in range(len(board[i])):
            if board[i][j] != ".":
                row_bucket[ord(board[i][j])-ord("0")-1] += 1
                if row_bucket[ord(board[i][j])-ord("0")-1] > 1:
                    return False
    # column check
    for j in range(len(board)):
        col_bucket = [0] * 9
        for i in range(len(board[j])):
            if board[i][j] != ".":
                col_bucket[ord(board[i][j])-ord("0")-1] += 1
                if col_bucket[ord(board[i][j])-ord("0")-1] > 1:
                    # print(col_bucket[ord(board[i][j])-ord("0")-1])
                    return False
    # 3 * 3 square
    boxes = [set() for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ".":
                continue
            idx = (i // 3) * 3 + j // 3
            if board[i][j] in boxes[idx]:
                return False
            boxes[idx].add(board[i][j])
    return True

board = [[".",".",".",".",".",".",".",".","2"],
         [".",".",".",".",".",".","6",".","."],
         [".",".","1","4",".",".","8",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".","3",".",".",".","."],
         ["5",".","8","6",".",".",".",".","."],
         [".","9",".",".",".",".","4",".","."],
         [".",".",".",".","5",".",".",".","."]]
print(f"Output: {isValidSudoku(board)}")