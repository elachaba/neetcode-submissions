class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        idxHash = {}

        for i in range(len(nums)):
            if nums[i] in idxHash:
                return [idxHash[nums[i]], i]
            idxHash[target - nums[i]] = i
        

