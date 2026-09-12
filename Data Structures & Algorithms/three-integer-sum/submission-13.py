class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i, x in enumerate(nums):
            x = nums[i]
            if x > 0:
                break
            if i > 0 and x == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                y = nums[l]
                z = nums[r]
                threeSum = x + y + z
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    output.append([x, y, z])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

            
        
        return output
        