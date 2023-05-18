N=int(input())
count=0
lst=[False for _ in range(N)]
lst_u=[False for _ in range(2*N-1)]
lst_d=[False for _ in range(2*N-1)]
def dfs(depth):
    global count
    if depth==N:
        count+=1
        return
    if depth==0:
        for i in range(N//2):
            lst[i]=True
            lst_u[i+depth]=True
            lst_d[depth-i+N-1]=True
            dfs(depth+1)
            lst[i]=False
            lst_u[i+depth]=False
            lst_d[depth-i+N-1]=False
        count*=2
        if N%2==1:
            i=N//2
            lst[i]=True
            lst_u[i+depth]=True
            lst_d[depth-i+N-1]=True
            dfs(depth+1)
            lst[i]=False
            lst_u[i+depth]=False
            lst_d[depth-i+N-1]=False
    else:
        for i in range(N):
            if not lst[i] and not lst_u[i+depth] and not lst_d[depth-i+N-1]:
                lst[i]=True
                lst_u[i+depth]=True
                lst_d[depth-i+N-1]=True
                dfs(depth+1)
                lst[i]=False
                lst_u[i+depth]=False
                lst_d[depth-i+N-1]=False
dfs(0)
print(count)