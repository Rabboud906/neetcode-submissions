class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        di = {}
        for char in s:
            if char not in dic:
                
                dic[char] = 1
            else:
                dic[char] += 1
        for char in t:
            if char not in di:
                
                di[char] = 1
            else:
                di[char] += 1
        return dic == di