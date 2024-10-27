n=int(input())
count=0
mi=[-1]*11
for i in range(n):
    cow, where=map(int,input().split())
    if mi[cow]==-1:
        mi[cow]=where
    else:
        if mi[cow]!=where:
            count+=1
            mi[cow]=where
print(count)