class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair not in pairs:
                pairs[num] = i
            else:
                return [pairs[pair],i]