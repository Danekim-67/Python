t=int(input())
for i in range(1, t+1):
    line1=input()
    line2=input()
    l1inl2=0
    for j in line2:
        if l1inl2<len(line1) and line1[l1inl2]==j:
            l1inl2+=1
    if l1inl2==len(line1):
        print(f"Case #{i}: {(len(line2)-len(line1))}")
    else:
        print(f"Case #{i}: IMPOSSIBLE")