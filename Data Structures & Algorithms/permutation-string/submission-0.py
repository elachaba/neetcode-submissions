class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = 26 * [0]
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
        l, r = 0, len(s1) - 1
        while r < len(s2):
            curr = s2[l: r + 1]
            windowCount = 26 * [0]
            for i in range(len(s1)):
                windowCount[ord(curr[i]) - ord("a")] += 1
            matches = 0
            for i in range(26):
                matches += 1 if s1Count[i] == windowCount[i] else 0
            if matches == 26:
                return True
            l += 1
            r += 1
        return False