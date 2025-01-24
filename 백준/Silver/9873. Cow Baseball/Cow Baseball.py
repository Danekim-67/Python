import sys
input=sys.stdin.readline
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort()
cnt=0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            xy=l[j]-l[i]
            yz=l[k]-l[j]
            if xy<=yz<=xy*2:
                cnt+=1
print(cnt)
