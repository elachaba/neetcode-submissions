class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        postfix = [1] * (len(nums) + 1)

        output = []
        
        for j in range(0, len(nums)):
            if j == 0:
                prefix[j + 1] = nums[j]
            else:
                prefix[j + 1] = prefix[j] * nums[j]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = nums[i]
            else:
                postfix[i] = postfix[i + 1] * nums[i]
            
        for i in range(1, len(nums) + 1):
            output.append(prefix[i - 1] * postfix[i])
        
        print(nums)
        print(postfix)
        print(prefix)
        
        return output