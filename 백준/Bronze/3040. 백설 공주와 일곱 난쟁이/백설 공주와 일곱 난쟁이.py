from itertools import combinations

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
g=int(input())
h=int(input())
i=int(input())

l=[a,b,c,d,e,f,g,h,i]
l2=list(combinations(l,7))
for i in l2:
    if sum(i)==100:
        for j in i:
            print(j)