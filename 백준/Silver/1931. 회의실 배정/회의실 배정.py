n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int, input().split())))
l.sort(key=lambda x: (x[1],x[0]))
endtime=0
count=0
for i, j in l:
    if i>=endtime:
        endtime=j
        count+=1
print(count)