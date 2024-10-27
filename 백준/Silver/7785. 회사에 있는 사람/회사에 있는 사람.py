n=int(input())
l=set()
for i in range(n):
    a,b=input().split()
    if a in l:
        l.remove(a)
    else:
        l.add(a)
l2=sorted(l,reverse=True)
print(*l2, sep="\n")