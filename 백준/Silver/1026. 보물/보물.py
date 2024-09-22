n=int(input())
l=list(map(int, input().split()))
l2=list(map(int, input().split()))
l.sort()
l2.sort(reverse=True)
answer=0
for i in range(n):
    answer+=l[i]*l2[i]
print(answer)