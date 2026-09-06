class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashNums = set()

        for num in nums:
            if num in hashNums:
                return True
            hashNums.add(num)
        
        return False