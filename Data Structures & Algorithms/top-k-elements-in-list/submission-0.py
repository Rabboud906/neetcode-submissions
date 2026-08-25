class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}

        for num in nums:
            if num not in data:
                data[num] = 1
            else:
                data[num] += 1

        sorted_data_desc = dict(
            sorted(data.items(), key=lambda item: item[1], reverse=True)
        )

        return list(sorted_data_desc.keys())[:k]
            
