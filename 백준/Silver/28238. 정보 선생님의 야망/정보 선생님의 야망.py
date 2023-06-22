import sys
input=sys.stdin.readline

if __name__=='__main__':
    n=int(input())
    plan=dict()
    for i in range(5):
        for j in range(i+1,5):
            plan[(i,j)]=[]
    for k in range(n):
        A=[*map(int, input().split())]
        for i in range(5):
            if not A[i]:
                continue
            for j in range(i+1,5):
                if not A[j]:
                    continue
                plan[(i,j)].append(k)
    ans=[]
    day=(0,1)
    for v in plan:
        if len(plan[v])>len(ans):
            ans=plan[v]
            day=v
    print(len(ans))
    print(*[1 if v in day else 0 for v in range(5)])