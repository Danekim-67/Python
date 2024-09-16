case=1
while True:
    l,p,v=map(int, input().split())
    if p==0 and l==0 and v==0:
        break
    else:
        a=v%p
        if l < v % p:
            a=l
        answer=0
        answer=(v//p)*l+a
        print(f"Case {case}: {answer}")
        case+=1