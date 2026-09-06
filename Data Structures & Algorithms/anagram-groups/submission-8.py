class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictAnagrams = {}
        for elt in strs:
            fingerPrint = [0]*26
            for s in elt:
                fingerPrint[ord(s) - ord("a")] += 1
            dictAnagrams[tuple(fingerPrint)] = dictAnagrams.get(tuple(fingerPrint), []) + [elt]
        
        return list(dictAnagrams.values())
