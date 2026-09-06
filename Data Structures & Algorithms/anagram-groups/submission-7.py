class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsDict = {}
        for string in strs:
            stamp = [0] * 26
            for char in string:
                stamp[ord(char) - ord('a')] = stamp[ord(char) - ord('a')] + 1
            if tuple(stamp) in anagramsDict:
                anagramsDict[tuple(stamp)].append(string)
            else:
                anagramsDict[tuple(stamp)] = [string]

        res = []
        for stamp in anagramsDict:
            res.append(anagramsDict[stamp])
    

        return res