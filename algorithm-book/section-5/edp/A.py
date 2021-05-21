# AtCoder EDP Contest-A Frog 1

dp = []

N = int(input())
H = list(map(int, input().split()))

for n in range(N):
    if n == 0:
        dp.append(0)
    elif n == 1:
        dp.append(abs(H[1] - H[0]))
    else:
        min_cost = min([
            dp[n-1] + abs(H[n] - H[n-1]),
            dp[n-2] + abs(H[n] - H[n-2])
        ])
        dp.append(min_cost)

print(dp[len(dp) - 1])
