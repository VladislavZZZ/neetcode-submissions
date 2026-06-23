class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bits  = [False for _ in range(len(nums))]
        for el in nums:
            if bits[el]:
                return el
            bits[el]= True