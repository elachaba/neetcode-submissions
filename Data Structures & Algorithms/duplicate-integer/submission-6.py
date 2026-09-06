class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for elt in nums:
            if elt in num_set:
                return True
            num_set.add(elt)
        
        return False
         