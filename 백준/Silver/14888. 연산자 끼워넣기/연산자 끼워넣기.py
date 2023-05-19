N=int(input())
A=list(map(int,input().split()))
oper_lst=list(map(int,input().split()))
bigsmall=[-10**9,10**9]
fn_lst=[None for _ in range(N-1)]
cout_lst=[0 for _ in range(4)]

def dfs(d):
    if d==N-1:
        num=cal()
        if num>bigsmall[0]:
            bigsmall[0]=num
        if num<bigsmall[1]:
            bigsmall[1]=num
        return
    for i in range(4):
        if cout_lst[i]<oper_lst[i]:
            fn_lst[d]=i
            cout_lst[i]+=1
            dfs(d+1)
            cout_lst[i]-=1
        
def cal():
    result=A[0]
    for i in range(N-1):
        if fn_lst[i]==0:
            result+=A[i+1]
        elif fn_lst[i]==1:
            result-=A[i+1]
        elif fn_lst[i]==2:
            result*=A[i+1]
        elif fn_lst[i]==3:
            if result<0:
                result=-((-result)//A[i+1])
            else:
                result=result//A[i+1]
    return result
dfs(0)
print(bigsmall[0])
print(bigsmall[1])