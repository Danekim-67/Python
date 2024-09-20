m,n,k=map(int,input().split())
l=[input() for i in range(m)]
l2=[]
q=""
for i in range(m):
    for j in range(k):
        for a in range(n):
            q+=l[i][a]*k
        l2.append(q)
        q=""
for i in range(len(l2)):
    print(l2[i])