def calculate(s: str) -> int:
    precedence = {'(': -1, '*': 1, '/': 1, '+': 0, '-': 0}

    compute = {
        '+': lambda b, a: a + b,
        '-': lambda b, a: a - b,
        '*': lambda b, a: a * b,
        '/': lambda b, a: int(a / b)
    }

    nums = []
    operators = []

    cur = 0
    for ch in s + '+':
        if ch == ' ':
            continue
        elif ch.isdigit():
            cur = cur * 10 + int(ch)
        elif ch == '(':
            operators.append('(')
        elif ch == ')':
            nums.append(cur)
            # compute the expression backwards after last (
            # assume the precedence is strictly increasing
            while operators[-1] != '(':
                nums.append(compute[operators.pop()](nums.pop(), nums.pop()))
            # pop out '('
            operators.pop()
            # replace the expression in () by cur
            cur = nums.pop()
        else:
            # ch is an operator
            # nums[-1] operators[-1] cur ch
            nums.append(cur)
            # compute nums[-2] operators[-1] nums[-1] if ch <= operators[-1]
            while operators and precedence[operators[-1]] >= precedence[ch]:
                nums.append(compute[operators.pop()](nums.pop(), nums.pop()))
            # operators is empty or ch > operators[-1]
            # add ch to operators
            operators.append(ch)

            # update cur
            cur = 0

    return nums[0]


print(calculate("6-42/2"))
