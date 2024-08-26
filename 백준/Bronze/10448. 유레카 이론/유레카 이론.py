repeat=int(input())
tri=[]
for i in range(1, 46):
    tri.append(i*(i+1)/2)

for i in range(repeat):
    n=int(input())
    check=0
    for j in tri:
        if check==1:
            break
        for k in tri:
            if check==1:
                break
            for l in tri:
                if j+k+l==n:
                    check=1
                    print("1")
                    break
    if check!=1:
        print("0")