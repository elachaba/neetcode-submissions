class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        i = 0
        while i < len(nums) - 1:
            x = nums[i]
            if x > 0:
                break
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
                    while l < len(nums) - 1 and nums[l] == y:
                        l += 1
                    while r  > 0 and nums[r] == z:
                        r -= 1
            while i < len(nums) - 1 and nums[i] == x:
                i += 1

            
        
        return output
        