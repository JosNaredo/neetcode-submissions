class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        l, r = 0, len(nums)-1
        if nums[r] == target:
            return r
        elif nums[l] == target:
            return l
        else:
            res = -1
        
        pivotl, pivotr = 0, len(nums)-1
        while pivotl < pivotr - 1:
            mid = (pivotl + pivotr) // 2
            if nums[pivotl] < nums[mid] and nums[pivotl] > nums[pivotr]:
                pivotl = mid
            elif nums[mid] < nums[pivotr] and nums[pivotl] > nums[pivotr]:
                pivotr = mid
            else:
                break

        while l <= r:
            if nums[l] > nums[r] and nums[l] < target:
                r = pivotl
                l += 1
            elif nums[l] > nums[r] and nums[l] > target:
                r -= 1
                l = pivotr
            else:
                r -= 1
                l += 1
            
            if nums[r] == target:
                res = r
                break
            elif nums[l] == target:
                res = l
                break
            else:
                res = -1
        
        return res