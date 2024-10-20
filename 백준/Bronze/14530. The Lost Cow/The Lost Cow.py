x, y = map(int, input().split())
a = x
dis, direct = 1, 1
idx = 1
ans = 0
while True:
    for _ in range(dis):
        a += direct
        ans += 1
        if a == y:
            print(ans)
            exit()
    idx *= 2     
    dis = abs(a-x) + idx 
    direct *= (-1)