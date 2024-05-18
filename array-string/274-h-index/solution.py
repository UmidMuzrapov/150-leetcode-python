class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        hIndex = 0

        for i, citation in enumerate(citations):
            if n - i >= citation:
                if citation > hIndex:
                    hIndex = citation
            else:
                return max(hIndex, n - i)
        
        return hIndex
