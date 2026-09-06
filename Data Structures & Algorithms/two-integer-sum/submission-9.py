class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        idxHash = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in idxHash:
                return [idxHash[diff], i]
            idxHash[n] = i
        

