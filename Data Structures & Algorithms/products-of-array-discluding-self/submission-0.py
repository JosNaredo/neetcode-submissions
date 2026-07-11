class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in range(len(nums)):
            num_ = 1
            for j in range(len(nums)):
                num = nums[j]
                if i != j:
                    num_ = num_ * num
            new_nums.append(int(num_))
        return new_nums