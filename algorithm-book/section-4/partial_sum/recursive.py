count = 0


def recursive(n: int, numbers: list, target_sum: int):
    global count

    count += 1
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
a = [100, 200, 300, 400]
W = 200

possible = recursive(N, a, W)
print(possible, count)
