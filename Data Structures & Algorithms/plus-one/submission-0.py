class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        for i in range(len(digits)):
            if digits[i] + 1 < 10:
                digits[i] = digits[i] + 1
                break
            else:
                digits[i] = 0
        else:
            digits.append(1)
        
        return digits[::-1]