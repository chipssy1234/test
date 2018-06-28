# https://qiita.com/drken/items/a5e6fe22863b7992efdb
# https://abc032.contest.atcoder.jp/tasks/abc032_d
import copy
N, W = map(int,input().split())
v = [0]*(N)
w = [0]*(N)

for i in range(N):
    v[i],w[i] = map(int,input().split())

# このように配列を初期化しないといけなかったらしい
#############################################
inf=float("inf")
dp=[[-inf for i in range(W+1)] for j in range(N+1)]
for i in range(W+1): dp[0][i]=0
#############################################

# dp = [[0]*(W+1)] * (N+1)
# for i in range(W+1):
#     dp[0][i] = 0

for i in range(N):
    for wh in range(W+1):
        if wh < w[i]:
            dp[i+1][wh] = copy.copy(dp[i][wh])
        else:
            dp[i+1][wh] = max(dp[i][wh], dp[i][W-w[i]] + v[i])

print(dp[N][W])
