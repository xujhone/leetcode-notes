class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        score = 0

        depth = 0

        for i, c in enumerate(s):
            if c == '(':
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == '(':
                    # this is true for '()' and AB
                    # for (AB), it computes Sa * 2 + Sb * 2
                    # which is equal to (Sa + Sb) * 2
                    score += 1 << depth

        return score
    