class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alfs = dict()
        i = 0
        size = len(s)
        max_subs = 1
        max_len=0
        for j in range(size):
            alfs[s[j]]= 1 + alfs.get(s[j],0)
            max_len=max(max_len,alfs[s[j]])
            while j-i-max_len+1 > k:
                alfs[s[i]]-=1
                i+=1
            max_subs = max(max_subs,j-i+1)
        return max_subs
