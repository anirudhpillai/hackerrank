class Solution(object):
    def hIndex(self, citations):
        buckets = [0] * (len(citations)+1)

        for c in citations:
            if c > len(citations):
                buckets[len(citations)] += 1
            else:
                buckets[c] += 1

        total = 0

        for i in reversed(range(len(buckets))):
            total += buckets[i]
            if total >= i:
                return i

        return 0

        """Without Bucket Sort
        citations.sort(reverse=True)

        result = 0

        for i, citation in enumerate(citations):
            if citation >= i + 1:
                result = i + 1

        return result
        """
