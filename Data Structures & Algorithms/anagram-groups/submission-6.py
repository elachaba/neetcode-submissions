class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_dict = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            
            count_dict[tuple(count)].append(string)
        

        return list(count_dict.values())
        