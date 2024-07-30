X, Y=map(int,input().split())

RevX_str = str(X)[::-1]
RevX = int(RevX_str)

RevY_str = str(Y)[::-1]
RevY = int(RevY_str)

sumRev = RevX + RevY

result_str = str(sumRev)[::-1]
result = int(result_str)

print(result)