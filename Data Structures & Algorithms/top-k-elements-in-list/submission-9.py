class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        heap = []
        for n, freq in count.items():
            heapq.heappush(heap, (freq, n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        
        return output
