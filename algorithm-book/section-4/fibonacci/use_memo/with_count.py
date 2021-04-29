memo = []
count = 0


def use_memo_with_count(N: int) -> int:

    global memo
    global count

    count += 1

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
            fibonacci_number = use_memo_with_count(
                N-1) + use_memo_with_count(N-2)

            memo[N] = fibonacci_number

    return fibonacci_number


print('answer:', use_memo_with_count(24))
print('count:', count)
