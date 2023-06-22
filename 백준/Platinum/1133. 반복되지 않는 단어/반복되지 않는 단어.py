import sys
input=sys.stdin.readline

def chk(u,K,lst):
    for i in range(1,K):
        for j in range(1,u+1):
            if lst[-j]!=lst[-u*i-j]:
                return True
    return False

def solve(K,N,A,lst):
    d=len(lst)
    if d==N:
        return lst
    for i in range(A):
        lst.append(i)
        u=1
        ok=True
        while u*K<=d+1:
            if not chk(u,K,lst):
                ok=False
                break
            u+=1
        if ok:
            res = solve(K,N,A,lst)
            if res !=None:
                return res
        lst.pop()
    return None

if __name__=='__main__':
    K,N,A=map(int,input().split())
    ans=solve(K,N,A,[])
    if ans==None:
        print(-1)
    else:
        for c in ans:
            print(chr(c+ord('A')),end='')
        print()