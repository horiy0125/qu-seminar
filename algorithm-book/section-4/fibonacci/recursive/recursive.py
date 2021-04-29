def recursive(N: int) -> int:
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return recursive(N-1) + recursive(N-2)


print('\n')
print('answer:', recursive(3))
print('\n')
