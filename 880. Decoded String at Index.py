class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:

        # len of decoded string so far
        stack = [0]
        # sum of stack
        l = 0

        for i, c in enumerate(s):
            if c.isdigit():
                l *= int(c)
                if stack[-1] > 0:
                    stack.append(-int(c))
                else:
                    stack[-1] *= int(c)

                if l >= k:
                    k %= stack[-2]
                    if k == 0:
                        k = stack[-2]
                    return self.decodeAtIndex(s, k)

            else:
                # c is a character
                if stack[-1] < 0:
                    stack.append(l + 1)
                else:
                    stack[-1] += 1
                l += 1
                if l == k:
                    return c
