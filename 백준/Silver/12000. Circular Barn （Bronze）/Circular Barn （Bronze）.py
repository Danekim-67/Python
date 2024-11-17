n = int(input())
r = [int(input()) for i in range(n)]
md = 10000000000000000
for i in range(n):
    td = 0
    for j in range(n):
        if j >= i:
            distance = j - i
        else:
            distance = n - i + j
        td += r[j] * distance
    md = min(md, td)
print(md)