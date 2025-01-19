n = int(input())
l = [int(input()) for _ in range(n)]
ans=0
def sol(i, num, res):
    global ans
    if i==n:
        return
    sol(i+1, num, res)
    for x,y in zip(str(num)[::-1], str(l[i])[::-1]):
        if int(x)+int(y)>=10:
            return
    ans=max(ans,res+1)
    sol(i+1, num+l[i],res+1)
sol(0, 0, 0)
print(ans)