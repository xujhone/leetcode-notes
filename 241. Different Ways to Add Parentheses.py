class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # each operator in expression (including sub-expressions)
        # can be last to be operated

        # divide and conquer + memoization

        # preprocessing the expression
        # split expression by non-digit characters
        # tokens include operators
        tokens = re.split(r'(\D)', expression)
        # transfer
        str2op = {'+': add, '-': sub, '*': mul}
        for i, token in enumerate(tokens):
            if token.isdigit():
                tokens[i] = int(token)
            else:
                tokens[i] = str2op[token]

        @lru_cache(None)
        # return all possible results for expression[lo:hi]
        def helper(lo, hi):

            if lo + 1 == hi:
                return [tokens[lo]]

            res = []

            # operators are at odd indices
            for mid in range(lo + 1, hi, 2):
                res.extend(tokens[mid](x, y) for x in helper(lo, mid) for y in helper(mid + 1, hi))

            return res

        return helper(0, len(tokens))
