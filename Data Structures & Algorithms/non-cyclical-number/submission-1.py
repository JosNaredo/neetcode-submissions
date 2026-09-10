class Solution:
    def isHappy(self, n: int) -> bool:
        existing_non_ones = []
        isT = True
        while isT:
            new_num = 0
            for num in str(n):
                new_num += int(num)**2
            
            if new_num == 1:
                return True
            
            n = int(new_num)    
            if n in existing_non_ones:
                isT = False
            existing_non_ones.append(int(new_num))
        
        return False
