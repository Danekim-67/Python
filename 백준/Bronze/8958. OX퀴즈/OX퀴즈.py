
n = int(input())
for i in range(n):
    result = input()
    score = 0
    O = 0
    for j in result:
        if j == 'O':
            O += 1
            score += O
        else:
            O = 0
    print(score)