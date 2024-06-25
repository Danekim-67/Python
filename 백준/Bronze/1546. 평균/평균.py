howmany=int(input())
l=(list(map(int,input().split())))
M=max(l)
for i in range (howmany):
    l[i]=(l[i]/M)*100
print(sum(l)/howmany)