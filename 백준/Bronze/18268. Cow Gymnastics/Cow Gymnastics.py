k, n=map(int, input().split())
l=[]
for i in range(k):
    l.append(list(map(int, input().split())))
count, count2=0, 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        for a in range(k):
            if l[a].index(i)<l[a].index(j):
                count+=1
            else:
                count-=1
        if count==k or count==(-k):
            count2+=1
        count=0
print(count2)