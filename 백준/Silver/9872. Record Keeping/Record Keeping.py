n=int(input())
l=[]
seet=[]
for i in range(n):
    a, b, c=input().split()
    cow=[a,b,c]
    l.append(sorted(cow))
l.sort()
check=[]
cnt=1
for i in range(len(l)-1):
    if l[i]==l[i+1]:
        cnt+=1
    else:
        check.append(cnt)
        cnt=1
check.append(cnt)
print(max(check))

