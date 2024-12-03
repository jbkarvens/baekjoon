import sys
input=sys.stdin.readline

V=int(input())
E=[None for _ in range(V+1)]
out=[0 for _ in range(V+1)]
for i in range(1,V+1):
    str=input()
    for j in range(V):
        if str[j]=='W':
            if E[j+1]==None:
                E[j+1]=i
            out[i]+=1

cnt_out,gosu = -1,-1
for i in range(1,V+1):
    if cnt_out<out[i]:
        gosu=i
        cnt_out=out[i]
if E[gosu]==None:
    print(1,gosu)
else:
    print(2,gosu)