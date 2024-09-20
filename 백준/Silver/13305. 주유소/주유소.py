n=int(input())
l=list(map(int,input().split()))
l2=list(map(int,input().split()))
price=0
oil=l2[0]
for i in range(n-1):
    if oil>=l2[i]:
        oil=l2[i]
    price+=oil*l[i]
print(price)