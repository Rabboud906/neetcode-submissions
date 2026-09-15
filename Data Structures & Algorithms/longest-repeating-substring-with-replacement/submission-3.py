class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        count = {}
        result = 0

        while right < len(s):

            # Add s[right] to the window
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1

            # Shrink window while invalid
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            # Window is valid
            result = max(result, right - left + 1)

            # Move right
            right += 1

        return result
