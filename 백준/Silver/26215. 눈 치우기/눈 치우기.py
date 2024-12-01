n=int(input())
l=list(map(int, input().split()))
answer=sum(l)
if len(l)==1 and l[0]<=1440:
    print(l[0])
elif len(l)==1 and l[0]>1440:
    print(-1)
else:
    l.sort(reverse=True)
    repeat=0
    list=l
    check=[0]
    check=set(check)
    while set(l)!=check and len(l)>1:
        repeat+=1
        if l[0]==0:
            del (l[0])
        else:
            l[0]=l[0]-1
        if l[1]==0:
            del (l[1])
        else:
            l[1]=l[1]-1
        l.sort(reverse=True)
    repeat+=l[0]
    if repeat>1440:
        print(-1)
    else:
        print(repeat)