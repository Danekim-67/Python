n=int(input())
res=0
l=list(map(int, input().split()))
for i in range(l[0]):
    used=[0]*n
    check=True
    num=i+1
    used[num-1]=1
    for j in range(len(l)):
        num=l[j]-num
        if num>n:
            used[0]=-1
            break
        used[num-1]=1

    for j in used:
        if j != 1:
            check=False
    if check:
        res=i+1
        break
ans=[0]*n
num=res
ans[0]=num
for i in range(len(l)):
    num=l[i]-num
    ans[i+1]=num
print(*ans)