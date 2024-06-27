input1=input()
input2=input()
input3=input()
resist=0
if input1=="black":
    resist+=0*10
elif input1=="brown":
    resist+=1*10
elif input1=="red":
    resist+=2*10
elif input1=="orange":
    resist+=3*10
elif input1=="yellow":
    resist+=4*10
elif input1=="green":
    resist+=5*10
elif input1=="blue":
    resist+=6*10
elif input1=="violet":
    resist+=7*10
elif input1=="grey":
    resist+=8*10
elif input1=="white":
    resist+=9*10
if input2=="black":
    resist+=0
elif input2=="brown":
    resist+=1
elif input2=="red":
    resist+=2
elif input2=="orange":
    resist+=3
elif input2=="yellow":
    resist+=4
elif input2=="green":
    resist+=5
elif input2=="blue":
    resist+=6
elif input2=="violet":
    resist+=7
elif input2=="grey":
    resist+=8
elif input2=="white":
    resist+=9
if input3=="black":
    resist=resist*1
elif input3=="brown":
    resist=resist*10
elif input3=="red":
    resist=resist*100
elif input3=="orange":
    resist=resist*1000
elif input3=="yellow":
    resist=resist*10000
elif input3=="green":
    resist=resist*100000
elif input3=="blue":
    resist=resist*1000000
elif input3=="violet":
    resist=resist*10000000
elif input3=="grey":
    resist=resist*100000000
elif input3=="white":
    resist=resist*1000000000
print(resist)