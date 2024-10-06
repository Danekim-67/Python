m=int(input())
n=int(input())
l=[]
for i in range(m, n+1):
    a=0
    if i>1:
        for j in range(2, i):
            if i%j==0:
                a+=1
                break
        else:
            if a==0:
                l.append(i)
if l:
    print(sum(l))
    print(min(l))
else:
    print("-1")