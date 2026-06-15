class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        height_st=[]
        max_area=0
        for i,h in enumerate(heights):
            min_h = i
            while height_st and height_st[-1][0]>h:
                prev_h, prev_i = height_st.pop()
                max_area = max(max_area,prev_h*(i-prev_i))
                min_h = prev_i
            height_st.append((h,min_h))
        for h, i in height_st:
            max_area = max(max_area, h*(len(heights)-i))
        return max_area