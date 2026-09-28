class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # since there is no Max Heap in python we are gonna multiply each number by -1 and use min heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = abs(heapq.heappop(stones)) #-9
            second = abs(heapq.heappop(stones)) #-6
            if second < first:
                heapq.heappush(stones, second - first)
        if len(stones) == 0:
            return 0
        return abs(stones[0])






    #    while(len(stones) >= 2):
    #     stones = sorted(stones, reverse = True)
    #     x = stones[0]
    #     y = stones[1]
    #     if x > y:
    #         stones.append(x-y)
    #     elif y > x: 
    #         stones.append(y-x)
    #     stones.remove(x)
    #     stones.remove(y)
    #    if len(stones) == 1:
    #         return stones[0]
    #    else:
    #         return 0


     
       