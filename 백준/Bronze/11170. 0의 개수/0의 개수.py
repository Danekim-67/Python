n=int(input())
for i in range (n):
    zero = 0
    a, b= map(int, input().split())
    for j in range (a, b+1):
        for k in str(j):
            if k=="0":
                zero+=1
    print(zero)