NUM=1000000
plst=[True for _ in range(NUM)]
j=2+2
while j<NUM:
    plst[j]=False
    j+=2
for i in range(3,NUM,2):
    if plst[i]:
        j=i+i
        while j<NUM:
            plst[j]=False
            j+=i

cout_p=[0 for _ in range(NUM)]
cout_p_4k1=[0 for _ in range(NUM)]
for i in range(2,NUM):
    if plst[i]:
        cout_p[i]=cout_p[i-1]+1
        if i%4==1 or i==2:
            cout_p_4k1[i]=cout_p_4k1[i-1]+1
        else:
            cout_p_4k1[i]=cout_p_4k1[i-1]
    else:
        cout_p[i]=cout_p[i-1]
        cout_p_4k1[i]=cout_p_4k1[i-1]
while True:
    L,U=map(int,input().split())
    remL,remU=L,U
    if L==U==-1:
        break
    if U<=0:
        U=L=1
    elif L<=0:
        L=1
    print(remL,remU,cout_p[U]-cout_p[L-1],cout_p_4k1[U]-cout_p_4k1[L-1])