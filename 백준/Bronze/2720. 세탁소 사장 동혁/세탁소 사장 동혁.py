repeat=int(input())
for i in range(repeat):
    a=int(input())
    print(a//25, end=" ")
    a=a-((a//25)*25)
    print(a // 10, end=" ")
    a = a - ((a // 10) * 10)
    print(a // 5, end=" ")
    a = a - ((a // 5) * 5)
    print(a // 1)