class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if not haystack:
            return -1

        # KMP

        m = len(needle)
        n = len(haystack)

        # Precompute pi array
        # pi[i] is the largest integer smaller than i such that
        # needle[0:pi[i]] is a suffix of needle[0:i]
        pi = [-1] * (m + 1)
        # prev = pi[i-1]
        prev = -1

        # pi[i] = pi^k[i-1] + 1 where k is the smallest integer
        # such that needle[pi^k[i-1]] == needle[i-1]

        for i in range(1, m + 1):
            while prev >= 0 and needle[prev] != needle[i - 1]:
                prev = pi[prev]
            prev += 1
            pi[i] = prev

        # Pattern matching
        k = 0
        for i in range(n):
            while k >= 0 and needle[k] != haystack[i]:
                k = pi[k]
            k += 1

            if k == m:
                # needle matches haystack[i-m+1: i+1]
                return i - m + 1

        return -1
