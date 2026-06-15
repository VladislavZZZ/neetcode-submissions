class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        size = len(matrix)*len(matrix[0])
        l,r = 0 , size
        while l<r:
            m = l+((r-l)//2)
            i, j = m//len(matrix[0]), m%len(matrix[0])
            if matrix[i][j] > target:
                r = m
            elif matrix[i][j] < target:
                l = m + 1
            else:
                return True
        return True if (l<size and matrix[len(matrix)-1][len(matrix[0])-1]==target) else False