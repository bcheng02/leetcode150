class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        
        
        for i, n in enumerate(strs):
            sortedStr = ''.join(sorted(n))
            if (sortedStr not in myMap):
                myMap[sortedStr] = [n]
            else:
                myMap[sortedStr].append(n)
        
        return myMap.values()
            