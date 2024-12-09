x1,y1,x2,y2=map(int, input().split())
x3,y3,x4,y4=map(int, input().split())

if x3<=x1 and x4>=x2:
    if y2>=y3 and y2<=y4:
        y2=y3

    elif y1>=y3 and y1<=y4:
        y1=y4
if y1>=y3 and y2<=y4:
    if x3<=x2 and x2<=x4:
        x2=x3
    elif x1>=x3 and x1<=x4:
        x1=x4
if x1>=x2 or y1>=y2:
    print(0)
else:
    print((x2-x1)*(y2-y1))
