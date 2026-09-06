class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, elt in enumerate(nums):
            if (target - elt) in indices:
                return [indices[target - elt], i]

            indices[elt] = i
 
        