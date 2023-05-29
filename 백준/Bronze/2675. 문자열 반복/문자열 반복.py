T=int(input())
for _ in range(T):
    P=''
    R,S=input().split()
    R=int(R)
    for i in range(len(S)):
        P+=R*S[i]
    print(P)