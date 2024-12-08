n=int(input())
l=list(map(int, input().split()))
e=0
o=0
for i in range(len(l)):
    if l[i]%2==0:
        e+=1
    else:
        o+=1
while o>e:
    o=o-2
    e=e+1
if o<e:
    print(2*o+1)
else:
    print(o+e)