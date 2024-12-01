a,b,c,=map(int, input().split())
if c-b==1 and b-a==1:
    print("0")
elif c-b==2 or b-a==2:
    print("1")
else:
    print("2")
maxl=0
if (c-b)>=(b-a):
    maxl+=c-b-1
else:
    maxl+=b-a-1
print(maxl)