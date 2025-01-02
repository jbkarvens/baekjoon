import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    gear=dict()
    for _ in range(n):
        s1,s2=input().strip().split()
        if s2 in gear:
            gear[s2]+=1
        else:
            gear[s2]=1
    res=1
    for g in gear:
        res*=(gear[g]+1)
    print(res-1)