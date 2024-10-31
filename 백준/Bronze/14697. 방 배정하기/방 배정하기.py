a, b, c, n=map(int, input().split())
for i in range(n//a+1):
    for j in range(n//b+1):
        for k in range(n//c+1):
            if a*i+j*b+k*c==n:
                print(1)
                exit()
print(0)