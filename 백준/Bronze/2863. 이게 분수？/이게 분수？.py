a,b=map(int, input().split())
c, d=map(int, input().split())
r1=a/c+b/d
r2=c/d+a/b
r3=d/b+c/a
r4=b/a+d/c
max_r=max(r1,r2,r3,r4)

if max_r==r1:
    print("0")
elif max_r==r2:
    print('1')
elif max_r==r3:
    print('2')
elif max_r==r4:
    print('3')