def factorial (n):
    f=1
    for i in range (1, n+1):
        f=f*i
    return (f)
n = int(input())
answer=0
num=factorial(n)
while True:
    if num%10!=0:
        print(answer)
        break
    elif num%10==0:
        answer+=1
        num//=10