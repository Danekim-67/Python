testcase=int(input())
for i in range (testcase):
    howmany1=int(input())
    l1=set(map(int,input().split()))
    howmany2=int(input())
    l2=list(map(int, input().split()))
    for j in l2:
        if j in l1:
            print(1)
        else:
            print(0)