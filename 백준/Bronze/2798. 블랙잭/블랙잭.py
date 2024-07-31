n, m = map(int, input().split())
cards = list(map(int, input().split()))

best = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= m and sum > best:
                best = sum

print(best)