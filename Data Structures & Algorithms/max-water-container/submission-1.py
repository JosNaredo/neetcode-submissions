class Solution:
    def maxArea(self, heights: List[int]) -> int:
        all_volumes = []
        l, r = 0, len(heights) - 1
        while l < r:
            volume = (r - l) * min([heights[l], heights[r]])        
            all_volumes.append(volume)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1

        return max(all_volumes)