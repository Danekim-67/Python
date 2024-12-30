n= int(input())
l=[]
for i in range(n):
    a, b=map(int, input().split())
    l.append((a, b))
l.sort()
r=1000000000000
cnt=0
infected=[]
for i in range(n):
    if l[i][1]==1:
        infected.append(l[i][0])
    if l[i][1]==0:
        if i-1>=0 and l[i-1][1]==1:
            r=min(r, l[i][0]-l[i-1][0])
        if i+1<n and l[i+1][1]==1:
            r=min(r, l[i+1][0]-l[i][0])
r -=1
for i in range(len(infected)-1):
    if infected[i+1] - infected[i]>r:
        cnt+=1
print(cnt+1)