n=int(input())
B=[0]*1001
for i in range(n):
    s, t, b=map(int, input().split())
    B[s]+=b
    B[t]-=b
bucket=0
result=0
for i in range(len(B)):
    bucket+=B[i]
    result=max(bucket, result)
print(result)