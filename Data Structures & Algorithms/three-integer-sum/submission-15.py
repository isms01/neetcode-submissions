class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_list = []
        for i, _ in enumerate(nums):
            for j in range(i+1,len(nums)-1):
                target = -1 * (nums[i] + nums[j])
                if target in nums[j+1:len(nums)]:
                    print(nums[i],nums[j],target)
                    candidate = sorted([nums[i],nums[j],target])
                    if candidate not in return_list:
                        return_list.append(candidate)
        return return_list