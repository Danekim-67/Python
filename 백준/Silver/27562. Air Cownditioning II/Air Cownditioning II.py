import itertools

n, m=map(int, input().split())
lc=[]
la=[]
for i in range(n):
    lc.append(list(map(int,input().split())))
for i in range(m):
    la.append(list(map(int, input().split())))
l=[0]*101
for i in range(n):
    for j in range(lc[i][0], lc[i][1]+1):
        l[j]=lc[i][2]
costs=[]
for i in range(1, m+1):
    use=itertools.combinations(la,i)
    use=list(use)

    for j in use:
        temp=[0]*101
        cost = 0
        for k in j:
            a, b, p, m = k
            for o in range(a, b+1):
                temp[o]-=p
            cost+=m
        check = True
        for k in range(101):
            if l[k]+temp[k]>0:
                check=False
        if check==True:
            costs.append(cost)
print(min(costs))
