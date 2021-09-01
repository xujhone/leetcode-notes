class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        # pair with smallest sum
        heap = [[nums1[0] + nums2[0], 0, 0]]

        res = []

        # rows[i] = True if some element in i-th row in the heap
        rows = [False] * m
        # cols[j] = True if some element in j-th col in the heap
        cols = [False] * n

        # heap != None to avoid error when k > len(nums1) * len(nums2)
        while heap and len(res) < k:
            # pair (nums1[i], nums2[j]) is popped out of heap
            _, i, j = heapq.heappop(heap)
            rows[i] = cols[j] = False
            res.append([nums1[i], nums2[j]])
            # consider next candidate: [i+1, j], [i, j+1]
            # note each row and col only need at most one candidate
            if j + 1 < n and not rows[i] and not cols[j + 1]:
                # [i, j+1] does not have candidate yet
                heapq.heappush(heap, [nums1[i] + nums2[j + 1], i, j + 1])
                rows[i] = cols[j + 1] = True
            if i + 1 < m and not rows[i + 1] and not cols[j]:
                # [i+1, j] does not have candidate yet
                heapq.heappush(heap, [nums1[i + 1] + nums2[j], i + 1, j])
                rows[i + 1] = cols[j] = True

        return res
