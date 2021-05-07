def recursive(n: int, numbers: list, target_sum: int):
    print(n, target_sum, numbers)
    if n == 0:
        return target_sum == 0
    else:
        results = [
            recursive(n-1, numbers, target_sum),
            recursive(n-1, numbers, target_sum - numbers[n-1])
        ]

        return True in results


N = 4
a = [3, 2, 6, 5]
W = 14

possible = recursive(N, a, W)
print(possible)
