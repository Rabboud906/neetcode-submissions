class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = math.sqrt(x ** 2 + y ** 2)
            closest.append((dist, point))
        heapq.heapify(closest)
        result = []

        for i in range(k):
            dist, point = heapq.heappop(closest)
            result.append(point)

        return result
        