import sys
sys.setrecursionlimit(10 ** 5)

memo = []


def tribonacci_memo(N: int) -> int:

    global memo

    if len(memo) == 0:
        for _ in range(N+1):
            memo.append(-1)

    tribonacci_number = memo[N]

    if tribonacci_number == -1:
        if N == 0 or N == 1:
            tribonacci_number = 0
        elif N == 2:
            tribonacci_number = 1
        else:
            tribonacci_number = tribonacci_memo(
                N - 1) + tribonacci_memo(N - 2) + tribonacci_memo(N - 3)

        memo[N] = tribonacci_number

    return tribonacci_number


print(tribonacci_memo(10 ** 4))
