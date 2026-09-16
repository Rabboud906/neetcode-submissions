class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1. Build a dictionary from s1
        dictionary_s1 = {}

        for char in s1:
            if char not in dictionary_s1:
                dictionary_s1[char] = 1
            else:
                dictionary_s1[char] += 1

        # 2. Iterate through s2 using a window
        right = 0

        while right <= len(s2) - len(s1):

            dictionary_window = {}

            for i in range(right, right + len(s1)):
                if s2[i] not in dictionary_window:
                    dictionary_window[s2[i]] = 1
                else:
                    dictionary_window[s2[i]] += 1

            # 3. Check if current window is a permutation
            if dictionary_window == dictionary_s1:
                return True

            right += 1

        return False
        