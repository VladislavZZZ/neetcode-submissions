class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        o1 = dict()
        for i in range(len(s)):
            if s[i] in o1.keys(): o1[s[i]]+= 1
            else: o1[s[i]]=1
            if t[i] in o1.keys(): o1[t[i]]-=1
            else: o1[t[i]]=-1
        return all(v==0 for v in o1.values())