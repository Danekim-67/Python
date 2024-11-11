from itertools import combinations
l=[]
n, m=map(int, input().split())
for i in range(1,n+1):
    l.append(i)
for i in combinations(l, m):
    print(*i)