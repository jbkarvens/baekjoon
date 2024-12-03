V=int(input())
E=[[] for _ in range(V+1)]
E_rev=[[] for _ in range(V+1)]
for i in range(1,V+1):
    for j,c in enumerate(input()):
        if c=="W":
            E[j+1].append(i)
            E_rev[i].append(j+1)

cnt,gosu = -1,-1
for i in range(1,V+1):
    if cnt<len(E_rev[i]):
        gosu=i
        cnt=len(E_rev[i])
if not E[gosu]:
    print(1,gosu)
else:
    print(2,gosu)