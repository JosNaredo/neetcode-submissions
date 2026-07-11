class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dic = {}
        for n in nums:
            if nums_dic.get(n) != None:
                nums_dic[n] += 1
            else:
                nums_dic[n] = 1

        nums_dic_sorted =  dict(sorted(nums_dic.items(), key=lambda x: x[1], reverse=True))
        return list(nums_dic_sorted.keys())[0:k]