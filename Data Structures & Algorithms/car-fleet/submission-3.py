class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,(target-p)/s] for p,s in zip(position, speed)]
        st = []
        for pair in sorted(pairs)[::-1]:
            st.append(pair[1])
            if len(st)>=2 and st[-1] <= st[-2]:
                st.pop()
        return len(st)

