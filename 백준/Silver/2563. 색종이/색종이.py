l=[[0]*100 for _ in range(100)]

for i in range (int(input())):
    x, y=map(int,input().split())
    for row in range(x,x+10):
        for col in range(y,y+10):
            l[row][col]=1
n=0
for i in range(100):
    n+=l[i].count(1)
print(n)