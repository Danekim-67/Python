e, s, m=map(int,input().split())
ea, sa, ma=1, 1, 1
year=1
while True:
    if ea==e and sa==s and ma==m:
        print(year)
        break
    year+=1
    ea=ea%15 +1
    sa=sa%28 +1
    ma=ma%19+1
