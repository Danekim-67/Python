while True:
    l=list(map(int,input().split()))
    count=0
    if l[0]==-1:
        break
    else:
        for i in range(len(l)):
            if l[i]*2 in l:
                if l[i]!=0:
                    count+=1
        print(count)