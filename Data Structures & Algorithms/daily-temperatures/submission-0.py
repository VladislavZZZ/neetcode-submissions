class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res=[0 for n in range(len(temperatures))]
        for i,cur_temp in enumerate(temperatures):
            while st and st[-1][0]<cur_temp:
                res[st[-1][1]] = i-st[-1][1]
                st.pop()
            st.append((cur_temp,i))
        return res