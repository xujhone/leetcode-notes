class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # let dp[i] be len of longest valid parentheses substring ending at s[i]
        # base case: dp[0] = 0, if s[i] == '(', dp[i] = 0
        # optimality relation:
        # note there are two types of valid parentheses: AB and (A)
        # if s[i-1] = '(' and s[i] = ')', dp[i] = dp[i-2] + 2
        # if s[i-1] = s[i] = ')', inner valid parentheses has len dp[i-1]
        # we need s[i-1-dp[i-1]] = '(', dp[i] = dp[i-1] + 2
        # we also add valid substring ending at s[i-1-dp[i-1]-1]
        # thus, dp[i] = dp[i-1] + 2 + dp[i-2-dp[i-1]]
        # note when s[i-1] = '(', i-2-dp[i-1] = i-2 and dp[i-1] = 0

        n = len(s)

        dp = [0] * n

        for i in range(1, n):
            if s[i] == ')' and i - 1 - dp[i - 1] >= 0 and s[i - 1 - dp[i - 1]] == '(':
                dp[i] = dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]]

        return max(dp, default=0)


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # bottom of stack is the index of last unpaired ')'
        # stack of indices of left parentheses
        stack = [-1]

        maxLen = 0

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                # top of stack is either index of last unpaired ')'
                # or index of '(' that is paired with c
                stack.pop()
                if stack:
                    # top of stack is index of unpaired '('
                    # i - stack[-1] is the len of longest valid parentheses
                    # ending at s[i]
                    maxLen = max(maxLen, i - stack[-1])
                else:
                    # s[i] is an unpaired ')'
                    stack.append(i)

        return maxLen


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        res = l = r = 0

        for c in s:
            if c == '(':
                l += 1
            else:
                r += 1

            if l == r:
                res = max(res, 2 * l)
            elif r > l:
                l = r = 0

        l = r = 0
        for c in reversed(s):
            if c == '(':
                l += 1
            else:
                r += 1

            if l == r:
                res = max(res, 2 * l)
            elif l > r:
                l = r = 0

        return res
