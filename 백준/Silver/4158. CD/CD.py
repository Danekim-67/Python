import sys
input=sys.stdin.readline
while True:
    count=0
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    list1=set([int(input()) for i in range(a)])
    for i in range(b):
        if int(input()) in list1:
            count+=1
    print(count)