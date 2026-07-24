class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # initial_areas = list(set(heights))
        
        # if 1 in heights:
        #     area_for_1 = [len(heights)]
        # else:
        #     area_for_1 = [0]
        
        created_areas = []
        for i in range(len(heights)):
            base_l = 0
            base_r = 0
            while i-base_l >= 0 and heights[i-base_l] >= heights[i]:
                base_l += 1
            while base_r+i <= len(heights)-1 and heights[i+base_r] >= heights[i]:
                base_r += 1
            created_areas.append((base_l + base_r - 1) * heights[i])
        return max(created_areas)