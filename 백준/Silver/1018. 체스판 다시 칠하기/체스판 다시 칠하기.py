n,m=map(int, input().split())
l=[]
res=50*50
for i in range(n):
    l.append(input())

for r in range(n-7):
    for c in range(m-7):
        wb=0
        bw=0
        for i in range(r, r+8):
            for j in range(c, c+8):
                if (i+j)%2==0:
                    if l[i][j]=="B":
                        wb+=1
                    if l[i][j]=="W":
                        bw+=1
                else:
                    if l[i][j]=="W":
                        wb+=1
                    if l[i][j]=="B":
                        bw+=1
        res=min(res, wb, bw)
print(res)