a, b, n=map(int, input().split())
l=[]
for i in range(n):
    cost, howmany=map(int, input().split())
    way=list(map(int,input().split()))
    if way.count(a)>0 and way.count(b)>0:
        if way.index(a)<way.index(b):
            l.append(cost)
if l:
    print(min(l))
else:
    print("-1")