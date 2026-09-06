class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevValues = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in prevValues:
                return [prevValues[diff], idx]
            prevValues[val] = idx
        
            
        