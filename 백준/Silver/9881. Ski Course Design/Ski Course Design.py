n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
res=9999999999999999
for i in range(101):
    tax=0
    for j in l:
        if j<i:
            tax+=(i-j)**2
        elif j>i+17:
            tax+=(j-i-17)**2
    if res>tax:
        res=tax
print(res)