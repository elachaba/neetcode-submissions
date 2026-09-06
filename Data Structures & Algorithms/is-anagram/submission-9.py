class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_char = [0] * 26
        zero = [0] * 26

        for i in range(len(s)):
            idxs = ord(s[i].lower()) - ord('a')
            idxt = ord(t[i].lower()) - ord('a')
            map_char[idxs] += 1
            map_char[idxt] -= 1
        
        return map_char == zero
