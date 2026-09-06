class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for curr in numSet:
            if curr - 1 not in numSet:
                length = 1
                while (curr + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest
        