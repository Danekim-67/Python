t=int(input())
for i in range(t):
    n = int(input())
    h=list(map(int,input().split()))
    answer=[]
    for j in range(len(h)-1):
        if h[j]==h[j+1]:
            answer.append(h[j])
    for j in range(len(h)-2):
        if h[j]==h[j+2]:
            answer.append(h[j])
    answer=set(answer)
    sorted_answer = sorted(answer)
    if answer:
        print(*sorted_answer)
    else:
        print("-1")