class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        l, r = 0, len(height) - 1
        # print((l,r))
        while height[l] < height[l+1]:
            # print(l)
            l += 1
        while height[r] < height[r-1]:
            # print(r)
            r -= 1
        if l == r or (l == 0  and r == 0):
            return 0
        # l += 1
        # r -= 1
        # print((l,r))
        count = 0
        position = []
        min_border = min(height[l], height[r])
        maximal_area = (r-l) * min_border
        area = 0
        for i in range(l, r):
            if height[i] > 0 and height[i] >= min_border:
                count += 1
                position.append(i)
                maximal_area -= min_border
            elif height[i] > 0 and height[i] < min_border:
                maximal_area -= height[i]
        
        new_height = [h-min_border if h-min_border >= 0 else 0 for h in height]
        valid = len([i for i in new_height if i != 0]) > 1
        while valid:
            l, r = 0, len(new_height) - 1
            while new_height[l] <= new_height[l+1]:
                l += 1
            while new_height[r] <= new_height[r-1]:
                r -= 1

            min_border = min(new_height[l], new_height[r])
            new_maximal_area = (r-l) * min_border
            if new_maximal_area > 0 and l != r:
                for i in range(l, r):
                    if new_height[i] > 0 and new_height[i] >= min_border:
                        new_maximal_area -= min_border
                    elif new_height[i] > 0 and new_height[i] < min_border:
                        new_maximal_area -= new_height[i]
            else:
                new_maximal_area = 0
            maximal_area += new_maximal_area
            new_height = [h-min_border if h-min_border >= 0 else 0 for h in new_height]
            valid = len([i for i in new_height if i != 0]) > 1

        return maximal_area 