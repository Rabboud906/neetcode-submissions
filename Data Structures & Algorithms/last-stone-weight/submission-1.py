class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
       while(len(stones) >= 2):
        stones = sorted(stones, reverse = True)
        x = stones[0]
        y = stones[1]
        if x > y:
            stones.append(x-y)
        elif y > x: 
            stones.append(y-x)
        stones.remove(x)
        stones.remove(y)
       if len(stones) == 1:
            return stones[0]
       else:
            return 0


     
       