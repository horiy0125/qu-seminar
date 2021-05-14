N = int(input())
a = list(map(int, input().split()))
W = int(input())


def judge_sum(index: int, current_sum: int) -> bool:

    new_sum = a[index] + current_sum

    if new_sum > W:
        return judge_sum(index + 1, current_sum)
    elif new_sum == W:
        return True
    elif index == len(a) - 1:
        return False
    else:
        results = [judge_sum(index + 1, current_sum),
                   judge_sum(index + 1, new_sum)]
        return True in results


print(judge_sum(0, 0))
