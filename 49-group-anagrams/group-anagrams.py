class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groupings = {}

        for i, val in enumerate(strs):
            sortedStr = ''.join(sorted(val))
            if (sortedStr in groupings):
                groupings[sortedStr].append(val)
            else:
                groupings[sortedStr] = [val]
        return groupings.values()
            
        