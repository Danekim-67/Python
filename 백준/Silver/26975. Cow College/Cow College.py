import sys
input=sys.stdin.readline
n= int(input())
l=[int(x) for x in input().split()]
l.sort()
maxx=0
tuition=l[0]
for i in range(n):
    noc=n-i
    a=l[i]
    total=noc*a
    if total>maxx:
        tuition=a
        maxx=total

print(maxx, tuition)
