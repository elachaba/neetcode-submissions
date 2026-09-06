class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for e in string:
                count[ord(e) - ord('a')] += 1
            
            str_dict[tuple(count)].append(string)
        
        return list(str_dict.values())

        