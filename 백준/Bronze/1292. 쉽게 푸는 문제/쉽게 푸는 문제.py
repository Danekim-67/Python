a, b=map(int, input().split())
l=[]
answer=0
for i in range(1, b+1):
    for j in range(i):
        l.append(i)
for i in range(a-1, b):
    answer+=l[i]
print(answer)