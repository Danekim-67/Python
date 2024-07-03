while True:
    n=int(input())
    r=0
    if n==0:
        break
    else:
        for i in range(1,n+1):
            r+=(n-i+1)**2
        print(r)