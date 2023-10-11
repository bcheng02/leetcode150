from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # declare a hashmap??
        map = defaultdict(list) # this is already {x: [], y: []...}
        
        # sort each str, collect them in hashmap
        for s in strs:
            sortedStr = tuple(sorted(s)) # sorted ret list, but keys need to be immutable
            map[sortedStr].append(s)
        
        # return values of hashmap
        
        return map.values()
        