import sys
sys.setrecursionlimit(10 ** 6)

memo = []


def use_memo(N: int) -> int:

    global memo

    if len(memo) == 0:
        for _ in range(N+1):
            memo.append(-1)

    if N == 0 or N == 1:
        fibonacci_number = memo[N]
        if fibonacci_number == -1:
            fibonacci_number = N
            memo[N] = fibonacci_number

    else:
        fibonacci_number = memo[N]
        if fibonacci_number == -1:
            fibonacci_number = use_memo(N-1) + use_memo(N-2)
            memo[N] = fibonacci_number

    return fibonacci_number


print(use_memo(24))
