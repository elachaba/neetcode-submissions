class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            for j in range(len(nums) - 1, i + 1, -1):
                for k in range(i + 1, j):
                    if nums[i] + nums[j] + nums[k] == 0:
                        combo = [nums[i], nums[k], nums[j]]
                        if combo not in res:
                            res.append(combo)
                        break
        return res
              