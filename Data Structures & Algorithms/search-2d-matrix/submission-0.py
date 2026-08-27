class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        start = 0
        end = len(matrix) - 1

        while start <= end:

            mid = (start + end) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return self.search(matrix[mid], target)

            elif matrix[mid][0] > target:
                end = mid - 1

            else:
                start = mid + 1

        return False


    def search(self, nums: List[int], target: int) -> bool:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False