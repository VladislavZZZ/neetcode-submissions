class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = stones
        heapq.heapify_max(self.heap)
        while len(self.heap) > 1:
            st1, st2 = heapq.heappop_max(self.heap), heapq.heappop_max(self.heap)
            if st1 != st2:
                heapq.heappush_max(self.heap, st1-st2)
        return self.heap[0] if len(self.heap) > 0 else 0
