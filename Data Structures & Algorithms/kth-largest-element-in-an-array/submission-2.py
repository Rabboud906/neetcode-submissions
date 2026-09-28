class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = sorted(nums, reverse = True)
        # return nums[k-1]
        biggest = [-s for s in nums]
        heapq.heapify(biggest)
        while k != 1:
            heapq.heappop(biggest)
            k = k - 1
        x = -1 * (heapq.heappop(biggest))
        return x

        
        