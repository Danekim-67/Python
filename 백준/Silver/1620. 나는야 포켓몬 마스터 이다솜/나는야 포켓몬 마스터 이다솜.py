n, m=map(int,input().split())
pokemon={}
onemore={}
for i in range(n):
    name=input()
    pokemon[i]=name
    onemore[name]=i
for i in range(m):
    solve=input()
    if solve.isdigit():
        print(pokemon[int(solve)-1])
    else:
        print(onemore[solve]+1)