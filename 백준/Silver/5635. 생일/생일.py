n=int(input())
l=[]
for i in range(n):
    n,d,m,y=input().split()
    d,m,y=int(d),int(m),int(y)
    l.append((y,m,d,n))
l.sort()
print(l[-1][3])
print(l[0][3])