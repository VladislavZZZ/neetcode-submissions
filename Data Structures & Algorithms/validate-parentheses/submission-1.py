class Solution:
    close= {")":"(","}": "{","]":"["}
    def isValid(self, s: str) -> bool:
        st = []
        for el in s:
            if el in self.close:
                if st  and st[-1] == self.close[el]:
                    st.pop()
                else:
                    return False
            else:
                st.append(el)
        return len(st) == 0