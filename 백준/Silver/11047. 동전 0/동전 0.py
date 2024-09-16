n,k=map(int,input().split())
l=[]
answer=0
for i in range(n):
    l.append(int(input()))
l.reverse()
for i in range(len(l)):
    if k>=l[i]:
        answer += k // l[i]
        k-=l[i]*(k//l[i])
print(answer)