class Solution:
    def counting(self, nums:List[int]) -> dict:
        counting = {}
        for num in nums:
            if num not in counting:
                counting[num] = 1
            else:
                counting[num] += 1
        return counting
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting = self.counting(nums)
        counting = sorted(counting, key=lambda x: counting[x], reverse=True)[:k]
        return counting