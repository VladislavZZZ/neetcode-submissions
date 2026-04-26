class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        head_link_count_map = dict()
        tail_link_map=dict()
        unique_nums = set()
        max_seq = 0
        for num in nums:
            if num in unique_nums:
                continue
            unique_nums.add(num)
            head_link_count_map[num] = 1
            tail_link_map[num] = num
            max_seq = max(max_seq, head_link_count_map[num])
            if num-1 in unique_nums:
                tail_link_map[num] = tail_link_map[num-1]
                head_link_count_map[tail_link_map[num]] +=1
                max_seq = max(max_seq, head_link_count_map[tail_link_map[num]])
                del tail_link_map[num-1]
                del head_link_count_map[num]
            if num+1 in unique_nums:
                if num in tail_link_map:
                    head_link_count_map[tail_link_map[num]] += head_link_count_map[num+1]
                    tail_link_map[num + head_link_count_map[num+1]] = tail_link_map[num]
                    max_seq = max(max_seq, head_link_count_map[tail_link_map[num]])
                    del tail_link_map[num]
                else:
                    tail_link_map[num + head_link_count_map[num+1]] = num
                    head_link_count_map[num] = head_link_count_map[num+1] + 1
                    max_seq = max(max_seq, head_link_count_map[num])
                del head_link_count_map[num+1]
        return max_seq