import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
l.sort()
for i in l2:
    low, high=0, n-1
    Flag=False
    while low<= high:
        mid=(low+high)//2
        if i==l[mid]:
            Flag=True
            print(1)
            break
        elif i>l[mid]:
            low=mid+1
        else:
            high=mid-1
    if not Flag:
        print(0)