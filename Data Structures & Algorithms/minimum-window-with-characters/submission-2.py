class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        alfsSum = 0
        if len(s) < len(t):
            return res
        alfs, alfs_check = dict(), dict()
        size = len(s)
        min_len=size
        i = 0
        for l in t:
            alfs[l] = 1 + alfs.get(l, 0)
            alfsSum += 1
        for j in range(size):
            if s[j] in alfs:
                alfs_check[s[j]] = 1 + alfs_check.get(s[j], 0)
                if alfs_check[s[j]] - alfs[s[j]] <= 0:
                    alfsSum -= 1
                if alfs_check[s[j]] - alfs[s[j]] >= 0:
                    while alfsSum == 0:
                        if min_len >= j - i + 1:
                            min_len = j - i + 1
                            res = s[i:j+1]
                        if s[i] in alfs:
                            if alfs_check[s[i]] - alfs[s[i]] <= 0:
                                alfsSum += 1
                            alfs_check[s[i]] -= 1
                        i += 1
        return res