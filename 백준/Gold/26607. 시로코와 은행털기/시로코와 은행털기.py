N, K, X = map(int, input().split())

dp = [set() for _ in range(K + 1)]
dp[0].add(0)

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(K - 1, -1, -1):
        for s in dp[i]:
            dp[i + 1].add(s + a)

ans = 0
for s in dp[K]:
    ans = max(ans, s * (K * X - s))

print(ans)