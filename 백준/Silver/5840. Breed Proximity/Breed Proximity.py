n, k=map(int, input().split())
cows=[]
check=[-1]*10000000
maxx=-1
for i in range(n):
    cows.append(int(input()))
for i in range(n):
    cow=cows[i]
    if check[cow]!=-1:
        if i-check[cow]<=k:
            maxx=max(maxx, cow)
    check[cow]=i
print(maxx)
