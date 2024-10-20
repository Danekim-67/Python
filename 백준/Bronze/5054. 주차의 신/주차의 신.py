n=int(input())
for i in range(n):
    long=int(input())
    l=list(map(int, input().split()))
    l.sort()
    print(abs((l[0]-l[long-1])*2))