from itertools import combinations

n, l, r, x=map(int, input().split())
l1=list(map(int, input().split()))
count=0
l1.sort()
for i in range(2, n+1):
    comb=list(combinations(l1, i))
    for j in comb:
        total=sum(j)
        maxd=max(j)
        mind=min(j)
        if l<=total and (maxd-mind)>=x and total<=r:
            count+=1
print(count)