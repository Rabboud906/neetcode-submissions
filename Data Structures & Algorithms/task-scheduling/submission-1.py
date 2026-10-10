class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-s for s in count.values()]
        # maxHeap = heapq.minHeap()
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()
        while q or maxHeap:
            time += 1
            if maxHeap:
                
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append([cnt, n + time])
            if q and q[0][1] == time:
                val = q.popleft()[0]
                if val:
                    heapq.heappush(maxHeap, val)
        return time



        
        
        