while True:
    a=True
    sentence=input()
    l=[]
    if sentence==".":
        break
    else:
        for i in sentence:
            if i=="(":
                l.append(i)
            if i=="[":
                l.append(i)
            if i==")":

                    if l and l[-1]=="(":
                        l.pop()
                    else:
                        print("no")
                        a=False
                        break
            if i=="]":
               
                    if l and l[-1]=="[":
                        l.pop()
                    else:
                        print("no")
                        a=False
                        break
    if a:
        if l:
            print("no")
        else:
            print("yes")