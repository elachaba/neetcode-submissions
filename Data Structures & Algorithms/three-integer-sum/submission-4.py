class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            k = i + 1
            j = len(nums) - 1
            while k < j:
                if nums[i] + nums[k] + nums[j] == 0:
                    combo = [nums[i], nums[k], nums[j]]
                    if not (combo in res):
                        res.append(combo)
                    j -= 1
                    k += 1
                    continue
                if nums[i] + nums[k] + nums[j] > 0:
                    j -= 1
                else:
                    k += 1
                
        return res
              