n=int(input())

for i in range(n):
    check=False
    l=list(map(int, input().split()))
    a=l[:4]
    b=l[4:]
    awinb=0
    bwina=0
    for x in a:
        for y in b:
            if x>y:
                awinb+=1
            elif x < y:
                bwina+=1
    if awinb==bwina:
        pass
    else:
        for j in range(1, 11):
            for k in range(1,11):
                for m in range(1,11):
                    for n in range(1,11):
                        c=[j,k,m,n]
                        cwinb, bwinc=0, 0
                        for x in c:
                            for y in b:
                                if x>y:
                                    cwinb+=1
                                elif x<y :
                                    bwinc += 1
                        cwina, awinc=0, 0
                        for x in c:
                            for y in a:
                                if x>y:
                                    cwina+=1
                                elif x < y :
                                    awinc+=1
                                   
                        if awinb > bwina :      
                            if cwina > awinc and cwinb < bwinc :
                                check = True
                        else :
                            if cwina < awinc and cwinb > bwinc :
                                check = True
                           

    if check:
        print("yes")
    else:
        print("no")
