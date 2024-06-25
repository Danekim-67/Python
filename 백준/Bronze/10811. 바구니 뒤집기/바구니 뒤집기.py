N, M=map(int, input().split())
l=[]
x=[]
for i in range (N):
    l.append(i+1)

for j in range(M):
    a, b=map(int, input().split())
    x=l[a-1:b]
    x.reverse()
    l[a-1:b]=x
print(*l)