n=int(input())
l=[[0]* 2001 for _ in range(2001)]
x=[0, 1, 0, -1]
y=[-1,0,1,0]
jx=1000
jy=1000
l[jx][jy]=1
res=1000000000
t=2

for i in range(n):
    dirr, dis=input().split()
    dis=int(dis)

    if dirr=="N":
        ind=2
    elif dirr=="S":
        ind=0
    elif dirr=="E":
        ind=1
    elif dirr=="W":
        ind=3
    for _ in range(dis):
        jxx =jx+x[ind]
        jyy=jy+y[ind]

        if l[jxx][jyy]!=0:
            res=min(res, t-l[jxx][jyy])
        l[jxx][jyy]=t
        jx=jxx
        jy=jyy
        t+=1
if res==1000000000:
    print(-1)
else:
    print(res)