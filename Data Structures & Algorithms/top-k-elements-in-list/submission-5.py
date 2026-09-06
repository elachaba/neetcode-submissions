class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for elt in nums:
            count[elt] = count.get(elt, 0) + 1

        for num, frequency in count.items():
            freq[frequency].append(num)
        
        res = []
        j = len(freq) - 1
        while j >= 0:
            for elt in freq[j]:
                res.append(elt)
                if len(res) == k:
                    return res
            j -= 1