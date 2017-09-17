
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """      
        if len(citations) == 0:
            return 0
        if len(citations) == 1:
            return min(1, citations[0])

        arr2 = [0 for i in range(len(citations) + 1)]
        # arr2[3]

        for citationCount in citations:
            if citationCount > len(citations):
                arr2[len(citations)] += 1
            else:
                arr2[citationCount] += 1



        numPapers = 0
        index = len(citations)

        # [
        while index >= 0:
            numPapers += arr2[index]
            if numPapers >= index:
                return index
            index -= 1
        return 0


Solution().hIndex([3, 0, 6, 1, 5])