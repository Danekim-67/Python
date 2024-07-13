n=int(input())
a=0
b=0
for i in range(1,n+1):
    a+=i*(i+1)
for i in range(1,n+1):
    for j in range(1,i+1):
        b+=j
print(a+b)