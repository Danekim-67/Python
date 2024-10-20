n=int(input())

for i in range(n):
    a, b=input().split()
    a=int(a)
    print(b[0:a-1]+b[a:] )