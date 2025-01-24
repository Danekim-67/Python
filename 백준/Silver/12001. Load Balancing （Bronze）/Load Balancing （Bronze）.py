n, b=map(int, input().split())
l=[]
xpo=[]
ypo=[]
for i in range(n):
    x, y= map(int, input().split())
    l.append((x,y))
    xpo.append(x)
    ypo.append(y)
check=[]
for i in range(n):
    for j in range(n):
        tr=0
        tl=0
        br=0
        bl=0
        l1=[]
        for k in range(n):
            if xpo[k]>xpo[i]+1 and ypo[k]<ypo[j]+1:
                br+=1
            if xpo[k]>xpo[i]+1 and ypo[k]>ypo[j]+1:
                tr+=1
            if xpo[k]<xpo[i]+1 and ypo[k]<ypo[j]+1:
                bl+=1
            if xpo[k]<xpo[i]+1 and ypo[k]>ypo[j]+1:
                tl+=1
        l1.append(br)
        l1.append(bl)
        l1.append(tr)
        l1.append(tl)
        check.append(max(l1))
print(min(check))