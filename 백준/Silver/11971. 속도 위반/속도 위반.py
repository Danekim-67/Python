n,m=map(int, input().split())
l=[]
l2=[]
l3=[]
for i in range(n):
    road, speed=map(int, input().split())
    for j in range(road):
        l.append(speed)
for i in range(m):
    road, speed=map(int, input().split())
    for j in range(road):
        l2.append(speed)
for i in range(100):
    l3.append(l2[i]-l[i])
if max(l3)<=0:
    print(0)
else:
    print(max(l3))