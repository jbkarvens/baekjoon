import sys
input=sys.stdin.readline
F=-1
q,b,e=[],0,-1
for _ in range(int(input())):
    s=input().split()
    if s[0]=='push':
        q.append(int(s[1]))
        e+=1
    elif s[0]=='pop':
        if b<=e:
            print(q[b])
            b+=1
        else:
            print(F)
    elif s[0]=='size': print(e-b+1)
    elif s[0]=='empty':
        if b<=e:
            print(0)
        else:
            print(1)
    elif s[0]=='front':
        if b<=e:
            print(q[b])
        else:
            print(F)
    elif s[0]=='back':
        if b<=e:
            print(q[e])
        else:
            print(F)