class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in seen:
                return [seen[need], i] if i > seen[need] else [i, seen[need]]
                
            else:
                seen[nums[i]] = i
        

#target = 7
# seen = { 0: 3, 1: 4, 2: 5, 3: 6}

