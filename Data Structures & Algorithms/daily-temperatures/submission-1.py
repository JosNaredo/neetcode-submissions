class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count_temp = []
        for i in range(len(temperatures)):
            count = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[i] >= temperatures[j]:
                    count += 1
                else:
                    count += 1
                    count_temp.append(count)
                    break
            else:
                count_temp.append(0)
        return count_temp