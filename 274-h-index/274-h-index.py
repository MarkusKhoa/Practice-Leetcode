class Solution(object):
    def hIndex(self, citations):
        if len(citations) == 0:
            return 0
        citations.sort(reverse = True)
        if citations[-1] >= len(citations):
            return len(citations)
        res = 0
        for i in range(0, len(citations) + 1):
            if i + 1 > citations[i]:
                res = i
                break
        return res