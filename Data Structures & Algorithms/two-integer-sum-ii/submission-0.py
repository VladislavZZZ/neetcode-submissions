class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i , j = 0 , len(numbers)-1
        while i<j:
            check_sum = numbers[i]+numbers[j]
            if check_sum > target:
                j-=1
            elif check_sum < target:
                i+=1
            else:
                return[i+1, j+1]