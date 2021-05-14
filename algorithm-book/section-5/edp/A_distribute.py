# N = int(input())
# H = list(map(int, input().split()))

# dp = [float('inf')] * (N + 2)

# for n in range(N-2):
#     if n == 0:
#         dp[0] = 0

#     one_step_cost = dp[n] + abs(H[n] - H[n+1])
#     two_step_cost = dp[n] + abs(H[n] - H[n+2])

#     if one_step_cost < dp[n+1]:
#         dp[n+1] = one_step_cost

#     if two_step_cost < dp[n+2]:
#         dp[n+2] = two_step_cost

# print(dp)
