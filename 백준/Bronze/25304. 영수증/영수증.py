totalp= int(input())
types=int(input())
totald=0
for i in range (1, types+1):
    a, b=map(int, input().split())
    totald=totald+(a*b)
if totald == totalp:
    print("Yes")
else:
    print("No")