n,m=map(int,input().split())
l=list(map(int,input().split()))
low=0
l.sort()
high=l[-1]
answer=0
while low<=high:
    mid=(low+high)//2
    t=0
    for i in l:
        if i>=mid:
            t+=i-mid
    if t<m:
        high=mid-1
    else:
        answer=mid
        low=mid+1
print(answer)