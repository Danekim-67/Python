n=int(input())
for i in range(n):
    c, v=map(int,input().split())
    print("You get",c//v,"piece(s) and your dad gets",c%v,"piece(s).")