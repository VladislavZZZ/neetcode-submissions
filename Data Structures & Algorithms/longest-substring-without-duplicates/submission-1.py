class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i, j = 0,0
        res = 1
        uniq_chars=set()
        size = len(s)
        while j<size:
            if s[j] not in uniq_chars:
                uniq_chars.add(s[j])
                res = max(len(uniq_chars),res)
                j+=1
            else:
                uniq_chars.remove(s[i])
                i+=1
        return res