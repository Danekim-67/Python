howmany=int(input())
a=0
for i in range(howmany+1, 0, -1):
    print(' '*a+"*"*(howmany*2-1))
    howmany-=1
    a+=1