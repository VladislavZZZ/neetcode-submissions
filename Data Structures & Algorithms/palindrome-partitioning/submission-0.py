class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,part = [],[]
        def isPali(s, i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        def getAllPalindromes(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPali(s, i,j):
                    part.append(s[i: j+1])
                    getAllPalindromes(j+1)
                    part.pop()
        getAllPalindromes(0)
        return res