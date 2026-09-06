class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxMap = {}

        for i, elt in enumerate(nums):
            diff = target - elt
            if diff in idxMap:
                return [idxMap[diff], i]
            idxMap[elt] = i
    
    