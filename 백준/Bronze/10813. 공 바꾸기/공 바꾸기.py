N, M=map(int, input().split())
l=[0]*N
for i in range (1, N+1):
    l[i-1]=i
for i in range (M):
    a, b = map(int, input().split())
    l[a-1],l[b-1]=l[b-1],l[a-1]
print(*l)