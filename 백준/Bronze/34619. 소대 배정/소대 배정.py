a, b, n ,k=map(int, input().split())
i=0
joongdae=1
sodae=1
inone=0
while i!=k:
    i+=1
    if inone<n:
        inone+=1
    else:
        if sodae<b:
            sodae=sodae+1
            inone=1
        else:
            joongdae+=1
            sodae=1
            inone=1
print(joongdae, end=" ")
print(sodae)