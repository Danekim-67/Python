n=int(input())
a=[0]*101
b=[0]*101
sinho=["" for _ in range(101)]
l=-1
r=-1
for i in range(n):
    sinho[i], a[i], b[i]=input().split()
    a[i]=int(a[i])
    b[i]=int(b[i])

    if sinho[i]=="none":
        if l==-1:
            l=i
        r=i
minn=-999999999
maxx=999999999

for i in range(1, n):
    if sinho[i]=="on":
        minn+=a[i]
        maxx+=b[i]

    elif sinho[i]=="off":
        minn= max(0, minn-b[i])
        maxx= max(0, maxx-a[i])

    else:
        minn=max(minn, a[i])
        maxx=min(maxx, b[i])

minn1=-int(1e9)
maxx1=int(1e9)

for i in range(r, -1, -1):
    if sinho[i]=="on":
        minn1=max(0, minn1-b[i])
        maxx1=max(0, maxx1-a[i])

    elif sinho[i]=="off":
        minn1+=a[i]
        maxx1+=b[i]

    else:
        minn1=max(minn1, a[i])
        maxx1=min(maxx1, b[i])
print(minn1, maxx1)
print(minn, maxx)