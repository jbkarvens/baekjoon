import sys
input=sys.stdin.readline

for c in range(int(input())):
    N,K=map(int, input().split())
    P=list(map(int, input().split()))
    P=list(set(P))
    P.sort()
    res=0
    win=[]
    for i in range(len(P)-1):
        win.append((P[i+1]-P[i])//2)
    win+=[P[0]-1,K-P[-1]]
    win.sort()
    res=win[-1]+win[-2]
    win2=[]
    for i in range(len(P)-1):
        win2.append(P[i+1]-P[i]-1)
    win2+=[P[0]-1,K-P[-1]]
    win2.sort()
    res=max(res,win2[-1])
    prob=res/K
    print(f'Case #{c+1}: '+str(prob))