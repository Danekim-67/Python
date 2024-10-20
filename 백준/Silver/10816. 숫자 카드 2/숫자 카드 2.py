import sys
input=sys.stdin.readline
n=int(input())
l=sorted(list(map(int,input().split())))
m=int(input())
l2=list(map(int,input().split()))
l3={}
for i in l:
    if i in l3:
        l3[i]+=1
    else:
        l3[i]=1
for i in l2:
    if i in l3:
        print(l3[i],end=" ")
    else:
        print(0, end= " ")