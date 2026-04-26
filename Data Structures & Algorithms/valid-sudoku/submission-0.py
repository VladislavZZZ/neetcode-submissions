class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set(["1","2","3","4","5","6","7","8","9"]) for _ in range(9)]
        column_sets = [set(["1","2","3","4","5","6","7","8","9"]) for _ in range(9)]
        submatr_sets = [[set(["1","2","3","4","5","6","7","8","9"]) for _ in range(3)]for _ in range(3)]
        for row in range(9):
            for column in range(9):
                if board[row][column] != ".":
                    if board[row][column] not in row_sets[row] or board[row][column] not in column_sets[column] \
                    or board[row][column] not in submatr_sets[row//3][column//3]:
                        return False
                    else:
                        row_sets[row].remove(board[row][column])
                        column_sets[column].remove(board[row][column])
                        submatr_sets[row//3][column//3].remove(board[row][column])
        return True