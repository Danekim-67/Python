import sys
input=sys.stdin.readline
n, s=map(int, input().split())
l=[]
for i in range(n):
    l.append(list(map(int, input().split())))
answer=0
location=s
power=1
direction=1
for i in range(1000000):
    if location-1<0 or location-1>=n:
        break
    if l[location-1][0]==1:
        if l[location-1][1]<=power:
            answer=answer+1
            l[location-1][0]=1000000000000
    elif l[location-1][0]==0:
        power+=l[location-1][1]
        if direction==1:
            direction=-1
        elif direction==-1:
            direction=1

    location+=(direction*power)
print(answer)