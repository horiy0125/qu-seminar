count = 0


def recursive_with_count(N: int):
    global count
    count += 1

    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return recursive_with_count(N-1) + recursive_with_count(N-2)


print('answer:', recursive_with_count(33))
print('count:', count)
