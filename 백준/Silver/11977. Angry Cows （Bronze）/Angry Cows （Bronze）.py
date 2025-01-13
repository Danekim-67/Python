n= int(input())
hay=[int(input()) for _ in range(n)]
hay.sort()
maxx=0
for i in range(n):
    exploded=[]
    r= i+1
    m=i
    rad=1
    res=1
    while True:
        if r>=n or hay[r]-hay[m]>rad:
            break
        while r<n and hay[r]-hay[m]<=rad:
            r+=1
            res+=1
        m=r-1
        rad+=1

    l=i-1
    m=i
    rad=1

    while True:
        if l<0 or hay[m]-hay[l]>rad:
            break
        while l>=0 and hay[m]-hay[l]<=rad:
            l-=1
            res+=1
        m=l+1
        rad+=1
    maxx=max(maxx, res)
print(maxx)