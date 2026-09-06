class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        optm = float('inf')
        def hours(piles, rate):
            val = 0
            for pile in piles:
                val += -(pile // -rate)
            
            return val
        
        max_rate = max(piles)
        l, r = 1, max_rate
        while l <= r:
            m = (l + r) // 2
            cost = hours(piles, m)
            if cost > h:
                l  = m + 1
            if cost <= h:
                if m < optm:
                    optm = m
                    r = m - 1
                else:
                    return optm
        
        return optm
            