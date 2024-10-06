import sys
input=sys.stdin.readline
n, q= map(int, input().split())
c=list(map(int, input().split()))
t=list(map(int, input().split()))
compare=[]
for i in range(len(c)):
    compare.append(c[i]-t[i])
compare.sort(reverse=True)
for i in range(q):
    v, s=map(int, input().split())
    if compare[v-1]>s:
        print("YES")
    else:
        print("NO")