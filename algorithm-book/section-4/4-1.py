def tribonacci(N: int) -> int:
    if N == 0 or N == 1:
        return 0
    elif N == 2:
        return 1
    else:
        return tribonacci(N - 1) + tribonacci(N - 2) + tribonacci(N - 3)


print('\n')
print('answer:', tribonacci(5))
print('\n')
