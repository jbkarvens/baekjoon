import sys
input_func=sys.stdin.readline

N=1000*2+1
M=50*2
binom=[[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N+1):
    binom[i][0] = 1
    for j in range(1,M+1):
        binom[i][j] = binom[i-1][j-1]+binom[i-1][j]
integral=[[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N+1):
    for j in range(min(i+1,M+1)):
        integral[i][j]=1/(binom[i][j]*(i+1))

def cal_integral(n1,m1,n2,m2):
    if m1==0:
        return 1/(n1+1)*(integral[n2][m2]-integral[n2+n1+1][m2])
    return -1/(n1-m1+1)*integral[n1+n2+1][m1+m2] + m1/(n1-m1+1)*cal_integral(n1,m1-1,n2,m2)

for _ in range(int(input_func())):
    n1,m1,n2,m2=map(int,input_func().split())
    denom = integral[n1][m1]*integral[n2][m2]
    numer = cal_integral(n1,m1,n2,m2)
    sys.stdout.write(f'{numer/denom}\n')