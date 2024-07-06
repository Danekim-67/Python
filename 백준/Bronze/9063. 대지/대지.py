a=int(input())
x1=[]
y1=[]
for i in range(a):
    x,y=map(int,input().split())
    x1.append(x); y1.append(y)
print((max(x1)-min(x1))*(max(y1)-min(y1)))