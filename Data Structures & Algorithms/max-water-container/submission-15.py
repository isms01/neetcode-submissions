class Solution:
    def maxArea(self, heights: List[int]) -> int:
        x_l, x_r = 0, len(heights)-1
        water_min = 0
        while x_l < x_r:
            x_diff = x_r - x_l
            y_min = min(heights[x_l], heights[x_r])
            water_tmp = x_diff * y_min
            if water_tmp > water_min:
                water_min = water_tmp

            if heights[x_l] <= heights[x_r]:
                x_l += 1
            else:
                x_r -= 1
        return water_min