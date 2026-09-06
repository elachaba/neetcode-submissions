class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def areAnagrams(s, t):
            if len(s) != len(t):
                return False
            countS, countT = {}, {}
            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)
            
            return countS == countT
        
        anagrams = []
        anagramExist = False
        for s in strs:
            if anagrams == []:
                anagrams.append([s])
            else:
                for strList in anagrams:
                    if areAnagrams(strList[0], s):
                        strList.append(s)
                        anagramExist = True
                        break
                if not anagramExist:
                    anagrams.append([s])
            anagramExist = False
        return anagrams
                    
        