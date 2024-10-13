n=int(input())
l=[]
size=[]
time=[0]*1001
for i in range(n):
    l.append(list(map(int, input().split())))
    for j in range(l[i][0], l[i][1]):
        time[j]+=1
for i in range(n):
    start=l[i][0]
    end=l[i][1]
    for j in range(start, end):
        time[j]-=1
    count=0
    for k in time:
        if k>0:
            count+=1
    size.append(count)
    for j in range(start, end):
        time[j]+=1
print(max(size))