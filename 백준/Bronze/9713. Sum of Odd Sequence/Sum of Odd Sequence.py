n=int(input())
for i in range(n):
    a=int(input())
    printthis=0
    for j in range(1,a+1):
        if j%2==0:
            j=j+1
        else:
            printthis=printthis+j
    print(printthis)