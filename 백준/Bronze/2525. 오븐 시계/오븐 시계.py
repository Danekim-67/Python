H, M = map(int, input().split())
cooktime=int(input())
if M+cooktime<60:
    print(H, M+cooktime)
elif M+cooktime>60:
    if (H+((M+cooktime)//60))>=24:
        print(H + ((M + cooktime) // 60)-24, ((M + cooktime) % 60))
    else:
        print(H + ((M + cooktime) // 60), ((M + cooktime) % 60))
elif M+cooktime==60:
    if (H + ((M + cooktime) // 60)) >= 24:
        print(H+((M + cooktime) // 60)-24, ((M + cooktime) % 60))
    else:
        print(H + 1, 0)