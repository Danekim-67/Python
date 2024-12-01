n,m=map(int, input().split())
setprice=[]
oneprice=[]
for i in range(m):
    a, b= map(int,input().split())
    setprice.append(a)
    oneprice.append(b)
setmin=min(setprice)
onemin=min(oneprice)
if setmin>=onemin*6:
    print(onemin*n)
elif setmin<onemin*6:
    if setmin<((n%6)*onemin):
        print(setmin*((n//6)+1))
    else:
        print((setmin*(n//6))+(onemin*(n%6)))