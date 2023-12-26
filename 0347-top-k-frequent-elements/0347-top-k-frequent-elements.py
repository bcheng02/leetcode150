class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        
        for i, n in enumerate(nums):
            if (n not in myMap):
                myMap[n] = 1
            else:
                myMap[n] += 1
        
        print(myMap)
        
        sortedMap = dict( sorted(myMap.items(), key = lambda x: x[1], reverse=True) ) 
        
        return list(sortedMap.keys())[0:k]
        
        