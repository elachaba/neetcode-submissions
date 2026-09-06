class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = 0
        hashSet = set(nums)
        for elt in hashSet:
            if (elt - 1) not in hashSet:
                length = 1
                while (elt + length) in hashSet:
                    length += 1
                seq = max(length, seq)
        
        
        return seq