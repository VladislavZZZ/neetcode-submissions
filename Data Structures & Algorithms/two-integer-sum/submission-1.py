class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_set = dict(zip([target-v for v in nums], [i for i in range(len(nums))]))
        for i in range(len(nums)):
            if nums[i] in new_set.keys() and i != new_set[nums[i]]:
                if i< new_set[nums[i]]: return [i,new_set[nums[i]]]
                else: return [new_set[nums[i]], i]