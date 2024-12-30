class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (not nums): return 0

        map = {}
        for num in nums:
            map[num] = False

        starts = []
        for num in nums:
            hasSmaller = num - 1 in map
            hasLarger = num + 1 in map
            if (hasLarger and not hasSmaller): starts.append(num)
        
        if (not starts): return 1
        else:
            maxLength = 0
            for start in starts:
                currLength = 0
                while(start in map):
                    currLength += 1
                    start += 1
                maxLength = max(maxLength, currLength)
            return maxLength


        # if (nums == []): return 0
        # map = {}
        # for num in nums:
        #     map[num] = False

        # start = None
        # for num in nums:
        #     hasSmaller = num - 1 in map
        #     hasLarger = num + 1 in map
        #     if (hasLarger and not hasSmaller): start = num

        # if start is None: 
        #     return 1
        # else:
        #     print(start)
        #     length = 0
        #     while(start in map):
        #         length += 1
        #         start += 1
        #     return length