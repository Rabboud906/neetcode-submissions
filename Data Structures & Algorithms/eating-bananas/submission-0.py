import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        k_low = 1
        k_high = max(piles)

        result = max(piles)

        while k_low <= k_high:

            mid = (k_low + k_high) // 2

            time = 0

            for pile in piles:
                time += math.ceil(pile / mid)

            if time > h:
                # eating too slowly
                k_low = mid + 1

            else:
                # mid works, remember it
                result = min(result, mid)

                # try a smaller eating speed
                k_high = mid - 1

        return result




"""
hour 
------ * banana
banana


"""