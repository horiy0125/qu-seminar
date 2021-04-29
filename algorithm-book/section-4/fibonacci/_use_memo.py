memo = []


def initialize_memo(N: int):
    for _ in range(N):
        memo.append(-1)


def use_memo(N: int) -> int:
    print(memo, N)
    return memo[N]


def write_memo(N: int, fibonacci_number: int):
    memo[N] = fibonacci_number


def compute_fibonacci_using_memo(N: int) -> int:

    if len(memo) == 0:
        initialize_memo(N)

    if N == 0:
        fibonacci_number = use_memo(N)
        if fibonacci_number == -1:
            fibonacci_number = 0
            write_memo(N, fibonacci_number)
    elif N == 1:
        fibonacci_number = use_memo(N)
        if fibonacci_number == -1:
            fibonacci_number = 1
            write_memo(N, fibonacci_number)
    else:
        fibonacci_number = use_memo(N)
        if fibonacci_number == -1:
            fibonacci_number = compute_fibonacci_using_memo(
                N-1) + compute_fibonacci_using_memo(N-2)
            write_memo(N, fibonacci_number)

    return fibonacci_number


print(compute_fibonacci_using_memo(5))

# for n in range(22):
#     print(compute_fibonacci_using_memo(n))
