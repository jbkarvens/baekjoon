prog=[]
def hanoi(n,a,b):
    if n==1:
        prog.append([a,b])
    else:
        tmp=[1,2,3]
        tmp.remove(a)
        tmp.remove(b)
        c=tmp[0]
        hanoi(n-1,a,c)
        prog.append([a,b])
        hanoi(n-1,c,b)
hanoi(int(input()),1,3)
print(len(prog))
for move in prog:
    print(*move)