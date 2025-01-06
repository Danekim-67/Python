import itertools
n=int(input())
blocks=[input() for _ in range(4)]
words=[input() for _ in range(n)]
for i in words:
    check=False
    for j in itertools.permutations(blocks, len(i)):
        same=True
        for k in range(len(i)):
            if i[k] not in j[k]:
                same=False
                break
        if same:
            check=True
            break
    if check:
        print("YES")
    else:
        print("NO")