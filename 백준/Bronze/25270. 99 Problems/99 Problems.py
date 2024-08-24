original=int(input())
originalup=original
originaldown=original
while True:
    originalup+=1
    if originaldown>0:
        originaldown-=1
    if "99" in (str(originalup%100)):
        print(originalup)
        break
    elif "99" in (str(originaldown%100)):
        print(originaldown)
        break