class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(list(set(nums)))
        print(sorted(sorted_nums))
        if len(sorted_nums) == 0:
            return 0

        consecutive, max_consecutive = 1, 1
        n = len(sorted_nums)
        for i in range(n-1):
            # break if index is last.

            if sorted_nums[i] == sorted_nums[i+1]-1:
                print(sorted_nums[i], sorted_nums[i+1])
                consecutive += 1
                max_consecutive = max(max_consecutive, consecutive)
            else:
                consecutive = 1
        return max_consecutive