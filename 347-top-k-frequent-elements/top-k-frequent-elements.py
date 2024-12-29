class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for i, val in enumerate(nums):
            freqMap[val] = freqMap.get(val, 0) + 1
        for n, c in freqMap.items():
            buckets[c].append(n)
        
        ans = []
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

        

