class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suff , preff = [], []
        for i in range(len(nums)):
            if i ==0:
                preff.append(nums[0])
                suff.append(nums[len(nums)-1])
            else:
                preff.append(preff[i - 1] * nums[i])
                suff.append(suff[i - 1] * nums[len(nums) - 1 - i])
        res = []
        for i in range(len(nums)):
            if i==0:
                res.append(suff[len(nums)-2])
            elif i==len(nums)-1:
                res.append(preff[len(nums)-2])
            else:
                res.append(preff[i-1]*suff[len(nums)-2-i])
        return res
