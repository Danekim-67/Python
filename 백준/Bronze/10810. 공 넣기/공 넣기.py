N, M=map(int, input().split())
l=[0]*N
for i in range (M):
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        l[i-1]=c
print(*l)