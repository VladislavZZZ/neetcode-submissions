class Solution:
    def trap(self, height: List[int]) -> int:
        suff, preff = [] , []
        curr_max = 0
        for bar in height:
            preff.append(max(bar,curr_max)) # 0,2,2,3,3,3,3,3,3,3
            curr_max = max(bar,curr_max)
        curr_max = 0
        size = len(height)
        for i in range(size):
            suff.append(max(height[size-1-i],curr_max)) # 1,2,3,3,3,3,3,3,3,3,3
            curr_max = max(height[size-1-i],curr_max)
        result = 0
        for bar, i in enumerate(height):
            result+=min(preff[bar],suff[size-1-bar])-i
        return result

        