x1,y1=map(int, input().split());x2,y2=map(int, input().split());x3,y3=map(int, input().split())
x=0;y=0
if x1==x2:
    x=x3
elif x2==x3:
    x=x1
elif x3==x1:
    x=x2
if y1==y2:
    y=y3
elif y2==y3:
    y=y1
elif y3==y1:
    y=y2
print(x, y)