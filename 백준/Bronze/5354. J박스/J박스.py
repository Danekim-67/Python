a=int(input())
for i in range(a):
    n=int(input())
    if n==1:
        print("#")
    else:
        print("#"*n)
        for j in range(n-2):
            print("#"+"J"*(n-2)+"#")
        print("#"*n)
    print()