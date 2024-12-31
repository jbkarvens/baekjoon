import sys
input=sys.stdin.readline

def solve(N,r,c):
    if N==1:
        if r==0:
            if c==0:
                return 0
            else:
                return 1
        else:
            if c==0:
                return 2
            else:
                return 3
    n=1<<(N-1)
    nn=1<<(2*N-2)
    if r<n:
        if c<n:
            return solve(N-1,r,c)
        else:
            return nn+solve(N-1,r,c-n)
    else:
        if c<n:
            return 2*nn+solve(N-1,r-n,c)
        else:
            return 3*nn+solve(N-1,r-n,c-n)

N,r,c=map(int,input().split())
print(solve(N,r,c))