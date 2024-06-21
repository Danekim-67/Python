howmany=int(input())
for i in range(1, howmany+1):
    a, b=map(int,input().split())
    print("Case #"+str(i)+":",(a+b))