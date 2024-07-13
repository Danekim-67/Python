while True:
    l=[]
    n=int(input())
    if n==0:
        break
    if n:
        while(n>=10):
            n=sum(map(int,list(str(n))))
        print(n)