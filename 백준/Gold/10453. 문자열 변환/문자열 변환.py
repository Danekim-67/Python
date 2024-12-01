n=int(input())
for i in range(n):
    a, b=input().split()
    aaindex=[j for j in range(len(a)) if a[j]=="a"]
    abindex=[j for j in range(len(a)) if a[j]=="b"]
    baindex=[j for j in range(len(b)) if b[j]=="a"]
    bbindex=[j for j in range(len(b)) if b[j]=="b"]
    if (len(aaindex)!=len(baindex)) or (len(abindex)!=len(bbindex)):
        print(-1)
    else:
        asum=0
        bsum=0
        for k in range(len(aaindex)):
            asum+=(abs(aaindex[k]-baindex[k]))
        for k in range(len(abindex)):
            bsum+=(abs(abindex[k]-bbindex[k]))
        print((asum+bsum)//2)