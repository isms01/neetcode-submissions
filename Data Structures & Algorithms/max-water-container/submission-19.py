class Solution:
    def maxArea(self, heights: List[int]) -> int:
        x_l, x_r = 0, len(heights)-1
        water_max = 0
        while x_l < x_r:
            water_max = max(water_max, (x_r - x_l) * min(heights[x_l], heights[x_r]))
            if heights[x_l] <= heights[x_r]:
                x_l += 1
            else:
                x_r -= 1
        return water_max