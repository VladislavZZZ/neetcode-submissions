class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = dict()
        order = [set(),set()]
        for num in nums:
            if num not in h_map:
                order[1].add(num)
                h_map[num] = 1
            else:
                if h_map[num]+1 >= len(order):
                    order.append(set())
                order[h_map[num]+1].add(num)
                order[h_map[num]].remove(num)
                h_map[num]+=1
        result = set()
        while len(result) < k:
            highest = order.pop()
            result |= highest
        return list(result)