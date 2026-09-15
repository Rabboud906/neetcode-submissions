class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_length = 0
        seen = set()
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                max_length = max(max_length, len(s[left:right]) )
            else:
                seen.remove(s[left])
                left+=1
        return max_length










"""
set = (z, x, y)  max_length = 3



"""
