l=[]
l=list(map(int, input().split()))
count=0
while True:
    count+=1
    check = 0
    for i in l:
        if count%i==0:
            check+=1
    if check>=3:
        break
print(count)