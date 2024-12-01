a, b=map(int, input().split())
num=0
while b>a:
    if b%2==0:
        b=b//2
    elif b%10==1:
        b=b//10
    else:
        break
    num+=1

if b==a:
    print(num+1)
else:
    print(-1)