class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        minbanana = 1
        maxbanana = max(piles)
        k = maxbanana
        while minbanana <= maxbanana:
            cut = (maxbanana + minbanana) // 2
            total_sum = sum(-(x // -cut) for x in piles)
            
            if total_sum <= h:
                maxbanana = cut - 1
                k = cut
                
            else:
                minbanana = cut + 1
        return k