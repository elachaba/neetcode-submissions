class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            total_time = 0
            for pile in piles:
                total_time += int(pile / k) + int(pile % k > 0)
            
            if total_time > h:
                l = k + 1
            else:
                res = k
                r = k - 1

        return res

