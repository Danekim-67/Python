s1, s2, s3=map(int,input().split())
l=[]
most=0
answer=0
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            l.append(i+j+k)
for i in l:
    if most<l.count(i):
        most=l.count(i)
        answer=i
print(answer)