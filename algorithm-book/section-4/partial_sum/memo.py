memo = []
count = 0


def use_memo(n: int, numbers: list, target_sum: int):
    global memo
    global count

    count += 1
    print(n, target_sum, numbers)

    if memo == []:
        col = [None] * (target_sum + 1)
        memo = [col] * (n + 1)

    if n == 0:
        return target_sum == 0
    else:
        this_memo = memo[n][target_sum]
        if this_memo != None:
            return this_memo
        else:
            result = False

            if use_memo(n-1, numbers, target_sum) or use_memo(n-1, numbers, target_sum - numbers[n-1]):
                result = True

            memo[n][target_sum] = result
            return result


N = 4
a = [100, 200, 300, 400]
W = 200

possible = use_memo(N, a, W)
print(possible, count)
