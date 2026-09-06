class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        noDuplicates = sorted(set(nums))
        res = 1
        seq = 1
        for i in range(1, len(noDuplicates)):
            if noDuplicates[i] - noDuplicates[i - 1] == 1:
                seq += 1
            else:
                if seq > res:
                    res = seq
                seq = 1
        if seq > res:
            res = seq
        
        return res