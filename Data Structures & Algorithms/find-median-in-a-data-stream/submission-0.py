class MedianFinder:

    def __init__(self):
        self.all_nums = []

    def addNum(self, num: int) -> None:
        self.all_nums.append(num)
        self.all_nums = sorted(self.all_nums)

    def findMedian(self) -> float:
        # if self.all_nums == []:
        #     return 
        if len(self.all_nums) % 2 == 0:
            return (self.all_nums[int(len(self.all_nums)/2 - 1)] + self.all_nums[int(len(self.all_nums)/2)]) / 2
        else:
            return self.all_nums[int(len(self.all_nums) // 2)]
        