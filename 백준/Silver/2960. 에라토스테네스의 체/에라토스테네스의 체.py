n, k= map(int, input().split())
number=[]
removed=[]
for i in range(2, n+1):
    number.append(i)
while number:
    a=1
    b=number[0]
    while b*a<=n:
        if b*a in number:
            removed.append(b*a)
            number.remove(b*a)
        a+=1
print(removed[k-1])