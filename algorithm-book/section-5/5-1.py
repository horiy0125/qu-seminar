N = int(input())
dp = [[-1, -1, -1]] * N

for day in range(N):
    if day == 0:
        dp[day] = list(map(int, input().split()))
    else:
        hapinesses = list(map(int, input().split()))

        dp[day] = [
            max([
                dp[day-1][1] + hapinesses[0],
                dp[day-1][2] + hapinesses[0]
            ]),
            max([
                dp[day-1][2] + hapinesses[1],
                dp[day-1][0] + hapinesses[1]
            ]),
            max([
                dp[day-1][0] + hapinesses[2],
                dp[day-1][1] + hapinesses[2]
            ])
        ]


print(max(dp[N-1]))
