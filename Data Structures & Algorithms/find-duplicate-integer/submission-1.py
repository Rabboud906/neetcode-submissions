class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # 1st Solution that got to mind and works 
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     else:
        #         seen.add(num)

        #2nd solution 
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]

        #needed solution
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
