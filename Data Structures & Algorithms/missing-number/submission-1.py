class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)+ 1):
            sum += i
        n_sum = 0
        for n in nums:
            n_sum += n
        return sum - n_sum