class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sort = []
        for num in nums:
            heapq.heappush(sort, num)
            if len(sort) > k:
                heapq.heappop(sort)
        return sort[0]
                