a=int(input())
if a%2==0:
    print("I LOVE CBNU")
else:
    print("*"*a)
    print(" "*(a//2)+"*")
    for i in range(1, a//2+1):
        print(str(" "*(a//2-i))+"*"+str(" "*(2*i-1))+"*")