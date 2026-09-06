class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for elt in nums:
            if elt in hashset:
                return True
            hashset.add(elt)
        
        return False
      