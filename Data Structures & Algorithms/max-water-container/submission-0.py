class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i , j = 0, len(heights)-1
        max_volume = 0
        while i!=j:
            volume = min(heights[i],heights[j])*(j-i)
            max_volume = max(max_volume, volume)
            if heights[j] >= heights[i]:
                i+=1
            else:
                j-=1
        return max_volume