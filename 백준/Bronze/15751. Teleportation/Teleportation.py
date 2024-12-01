a, b, x, y=map(int,input().split())
d=abs(a-b)
abl=[a,b]
abl.sort()
xyl=[x,y]
xyl.sort()
go=abs(xyl[0]-abl[0])+abs(xyl[1]-abl[1])
al=[d,go]
answer=min(al)
print(answer)