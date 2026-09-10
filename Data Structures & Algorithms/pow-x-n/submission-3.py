class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1
        if x == 0:
            return 0

        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1

        
        if n < 0:
            n = -n
            x = 1/x

        res = 1.0
        current = x
        
        while n > 0:
            if n % 2 != 0:
                res *= current
            
            current *= current
            
            n >>= 1
            # res *= x

        return res