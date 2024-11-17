n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int, input().split())))
l.sort()
time=0
for i in range(n):
    if time<l[i][0]:
        time=l[i][0]
    time+=l[i][1]
print(time)