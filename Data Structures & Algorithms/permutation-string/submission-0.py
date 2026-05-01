class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j = 0,len(s1)-1
        alfs=dict()
        if len(s2)<len(s1):
            return False
        for letter in s1:
            alfs[letter] = 1 + alfs.get(letter,0)
        while j<len(s2):
            cur_alfs = dict()
            isIncl = True
            for i in range(j-len(s1)+1,j+1):
                cur_alfs[s2[i]] = 1+cur_alfs.get(s2[i],0)
                if s2[i] not in alfs:
                    j=i+len(s1)-1
                    isIncl= False
                    break
                elif alfs[s2[i]]-cur_alfs[s2[i]]<0:
                    isIncl= False
                    break
            if isIncl:
                return True
            j+=1
        return False