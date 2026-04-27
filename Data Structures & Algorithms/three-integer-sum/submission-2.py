class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = set()
        i, j, k = 0, len(nums)-1, 1
        while i!=j:
            if k==j:
                i+=1
                k=i+1
                j=len(nums)-1
                continue
            sumOf2 = nums[i]+nums[j]
            if nums[k] + sumOf2==0:
                solutions.add((nums[i],nums[k],nums[j]))
                k+=1
            elif nums[k] + sumOf2 < 0:
                k+=1
            else:
                j-=1
                k=i+1
        return list(solutions)





        