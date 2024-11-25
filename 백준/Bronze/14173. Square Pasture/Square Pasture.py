x1, y1, x2, y2=map(int, input().split())
x3, y3, x4, y4=map(int, input().split())
sl1=[x1, x3]
sl2=[y1, y3]
bl1=[x2, x4]
bl2=[y2, y4]
if (max(bl1)-min(sl1))>(max(bl2)-min(sl2)):
    print((max(bl1)-min(sl1))**2)
else:
    print((max(bl2)-min(sl2))**2)