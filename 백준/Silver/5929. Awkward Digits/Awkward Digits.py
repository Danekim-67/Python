b2=list(input())
b3=list(input())
for i in range(len(b2)):
    for j in ["0", "1"]:
        if b2[i]!=j:
            b2l=list(b2)
            b2l[i]=j
            b2l=("".join(b2l))
            b10=int(b2l, 2)
            for k in range(len(b3)):
                for l in ["0", "1","2"]:
                    if b3[k]!=l:
                        b3l=list(b3)
                        b3l[k]=l
                        b3l=("".join(b3l))
                        b102=int(b3l, 3)

                        if b10==b102:
                            print(b10)
                            exit()
