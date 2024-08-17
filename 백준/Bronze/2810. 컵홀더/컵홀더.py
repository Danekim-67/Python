seats=int(input())
how=input()
LLnum=how.count("LL")
if LLnum<=1:
    print(seats)
else:
    print(seats-LLnum+1)