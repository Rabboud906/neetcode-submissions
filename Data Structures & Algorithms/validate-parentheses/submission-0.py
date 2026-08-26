class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        stack = []

        for char in s:
            if char in dictionary.keys():
                stack.append(char)
            else:
                if len(stack) != 0:
                    opening = stack.pop()

                    if dictionary[opening] != char:
                        return False
                else:
                    return False

        return len(stack) == 0
        