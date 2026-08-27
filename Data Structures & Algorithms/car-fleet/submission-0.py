class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []
        for pos, spe in cars: 
            miles = target - pos
            time = miles / spe
            if len(stack) == 0:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
        return len(stack)


"""
position = [7, 4, 1, 0]
speed    = [1, 2, 2, 1]
target   = 10

stack = [3, 4.5, 10]
"""