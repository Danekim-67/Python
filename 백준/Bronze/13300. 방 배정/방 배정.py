n, k=map(int,input().split())

students=[[0]*2 for i in range(6)]
for i in range(n):
    a, b=map(int, input().split())
    students[b-1][a-1]+=1
room=0

for i in range (6):
    for j in range(2):
        if (students[i][j]%k==0):
            room+=students[i][j]//k
        else:
            room+=students[i][j]//k+1
print(room)