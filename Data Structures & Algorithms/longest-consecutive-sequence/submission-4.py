class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums_set = list(sorted(set(nums)))
        count = 1
        count_f_count = []
        num_ = nums_set[0]
        for i in range(1, len(nums_set)):
            if num_ + 1 == nums_set[i]:
                count += 1
            else:
                count_f_count.append(count)
                count = 1
            num_ = nums_set[i]
        count_f_count.append(count)
        return list(sorted(count_f_count, reverse=True))[0]