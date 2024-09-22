n=int(input())
l=[]
l2=[]
for i in range(n):
    a, b=map(str, input().split())
    l.append([int(a),i,b])
l.sort()
for i in range(len(l)):
    print(l[i][0],l[i][2])