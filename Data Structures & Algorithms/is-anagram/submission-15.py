class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapS = [0] * 26
        mapT = [0] * 26

        for i in range(len(s)):
            mapS[ord(s[i]) - ord('a')] += 1
            mapT[ord(t[i]) - ord('a')] += 1
        
        return mapT == mapS
  