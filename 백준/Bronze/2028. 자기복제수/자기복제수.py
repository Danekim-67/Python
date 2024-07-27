howmany=int(input())
for i in range(howmany):
    n=int(input())
    mul=n*n
    num=len(str(n))
    if str(mul)[-num:]==str(n):
        print("YES")
    else:
        print("NO")