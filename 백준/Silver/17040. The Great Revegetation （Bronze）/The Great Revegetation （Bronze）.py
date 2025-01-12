n, m=map(int, input().split())
l=[]
for i in range(m):
    l.append(list(map(int, input().split())))
l2 = [[] for _ in range(n + 1)]
for a, b in l:
    l2[a].append(b)
    l2[b].append(a)

result = [0] * (n + 1)

p = 1

while p <= n:
    g = False
    for i in range(1, 5):
        check = True

        for j in l2[p]:
            if result[j] == i:
                check = False
                break

        if check:
            result[p] = i
            g = True
            break

    if not g:
        p -= 1
        result[p] = 0
    else:
        p+= 1
for i in range(1, len(result)):
    print(result[i], end="")
