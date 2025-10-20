a, b= map(int, input().split())
totalk=0
wheng=0
check=a
this=0
glist=[]
while b>2**this:
    this+=1
if 2**this!=b or a%2==0:
    print("-1")
else:
    while b!=2**(totalk):
        totalk+=1
    while a>1:
        wheng=0
        while a>2**wheng:
            wheng+=1
        a=a-2**(wheng-1)
        glist.append(wheng-1)
    if len(glist)>=1:
        print("G", end="")
        for i in range(totalk):
            check = False
            for j in glist:
                if i==j:
                    check=True
            if check==True:
                print("GK", end="")
            else:
                print("K", end="")
    else:
        print('G'+"K"*totalk)