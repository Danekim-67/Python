t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    count = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            if (a * a + b * b + m) % (a * b) == 0:
                count += 1
    print(count)