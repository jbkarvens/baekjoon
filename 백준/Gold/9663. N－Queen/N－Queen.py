N=int(input())
count=0
def dfs(depth,lst,lst_u,lst_d):
    global count
    if depth==N:
        count+=1
        return
    if depth==0:
        for i in range(N//2):
            dfs(depth+1,lst+[i],lst_u+[i+depth],lst_d+[i-depth])
        count*=2
        if N%2==1:
            i=N//2
            dfs(depth+1,lst+[i],lst_u+[i+depth],lst_d+[i-depth])
    else:
        for i in range(N):
            if not i in lst and not i+depth in lst_u and not i-depth in lst_d:
                dfs(depth+1,lst+[i],lst_u+[i+depth],lst_d+[i-depth])
dfs(0,[],[],[])
print(count)