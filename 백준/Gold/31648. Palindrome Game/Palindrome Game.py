import sys
input=sys.stdin.readline
n=int(input())
for i in range(n):
    a=int(input())
    count=0
    if a<10:
        print("B")
    elif a%10==0:
        print("E")
    else:
        print("B")