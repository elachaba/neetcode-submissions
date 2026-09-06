class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def getMostFreq(mapVal):
            maximum = -1000
            ret = 0
            for key in mapVal:
                if mapVal[key] >= maximum:
                    ret = key
                    maximum = mapVal[key]
            
            return ret
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        answer = []
        for i in range(k):
            key = getMostFreq(freqMap)
            del freqMap[key]
            answer.append(key)
        
        return answer
        
        