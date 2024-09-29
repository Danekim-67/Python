n=int(input())
S1=[]
S2=[]
C=[]
for i in range(n):
    s1, s2, c=map(int, input().split())
    S1.append(s1)
    S2.append(s2)
    C.append(c)
answer=[]
for i in range(3):
    shells=[0, 0, 0]
    shells[i]=1
    score=0
    for j in range(n):
        temp= shells[S1[j]-1]
        shells[S1[j]-1]=shells[S2[j]-1]
        shells[S2[j]-1]=temp
        if shells[C[j]-1]==1:
            score+=1
    answer.append(score)
print(max(answer))