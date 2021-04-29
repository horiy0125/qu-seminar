def compute_fibonacci_recursive(N: int) -> int:
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return compute_fibonacci_recursive(N-1) + compute_fibonacci_recursive(N-2)


# print(compute_fibonacci_recursive(3))

for n in range(22):
    print(compute_fibonacci_recursive(n))
