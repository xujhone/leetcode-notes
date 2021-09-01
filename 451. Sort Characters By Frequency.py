class Solution:
    def frequencySort(self, s: str) -> str:
        freq = collections.Counter(s)

        # put c * f together
        # for c, f in freq in reverse order of f

        # bucket[i] = \sum_{f==i} c * f
        bucket = [''] * (max(freq.values()))

        for c, f in freq.items():
            bucket[f - 1] += c * f

        return ''.join(reversed(bucket))
