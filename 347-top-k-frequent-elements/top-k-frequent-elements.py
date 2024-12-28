class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for i, val in enumerate(nums):
            freqMap[val] = freqMap.get(val, 0) + 1

        freqMap = dict( sorted(freqMap.items(), key = lambda x: x[1], reverse=True) )
        return list(freqMap.keys())[0:k] 