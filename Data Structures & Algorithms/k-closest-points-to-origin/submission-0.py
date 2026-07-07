class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        far_most = 20000
        def get_len(p):
            return math.sqrt(p[0]*p[0] + p[1]*p[1])
        for point in points:
            leng = get_len(point)
            if len(res) < k or (len(res) >= k and leng < far_most): 
                heapq.heappush_max(res, (leng,point))
                if len(res) > k:
                    heapq.heappop_max(res)
                far_most = res[0][0]
        return [r[1] for r in res]