class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board) , len(board[0])
        path = set()
        def isExist(i , j, letter_num):
            if letter_num == len(word):
                return True
            if i<0 or j<0 or i>=n or j>=m or (i,j) in path or board[i][j] != word[letter_num]:
                return False
            
            path.add((i,j))
            res = (isExist(i+1, j, letter_num+1) or isExist(i-1, j, letter_num+1) or isExist(i, j+1, letter_num+1) or isExist(i, j-1, letter_num+1))
            path.remove((i,j))
            return res
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and isExist(i,j, 0):
                    return True
        return False
